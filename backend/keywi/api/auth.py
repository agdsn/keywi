from datetime import timedelta, datetime
from typing import Optional
from urllib.parse import parse_qs, urlencode, urlunparse, urlparse

from authlib.integrations.base_client import OAuthError
from authlib.integrations.starlette_client import OAuth
from authlib.oauth2.rfc6749.util import scope_to_list, list_to_scope
from fastapi import Depends, HTTPException, status, APIRouter, Query
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, SecurityScopes
from fastapi_sqlalchemy import db
from jose import jwt, JWTError
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import RedirectResponse

from lib.app_config import app_config
from model import User
from model.session import session

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = app_config.get('general', 'jwt_secret')
ALGORITHM = "HS256"
access_token_expires = timedelta(days=14)

class TokenData(BaseModel):
    login: Optional[str] = None


group_scopes = {
    'rw-admin': [
        'user:read', 'user:write',
        'location:read', 'location:write',
        'lock:read', 'lock:write',
        'key:read', 'key:write',
        'rental:read', 'rental:write',
        'safe:read', 'safe:write',
        'log:read',
    ],
    'ro-admin': [
        'user:read',
        'location:read',
        'lock:read',
        'key:read',
        'rental:read',
        'safe:read',
        'log:read',
    ],
    'user': [
        'user:self:read',
        'location:read',
        'lock:read',
        'key:read',
        'rental:self:read',
        'safe:read',
        'log:self:read',
    ],
}

def url_add_parameters(url, params):
    """Adds parameters to URL, parameter will be repeated if already present"""
    if params:
        fragments = list(urlparse(url))
        value = parse_qs(fragments[4])
        value.update(params)
        fragments[4] = urlencode(value)
        url = urlunparse(fragments)
    return url

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




async def get_current_user(security_scopes: SecurityScopes,
                           token: str,
                           ignore_scope_error: bool):
    scope = ''

    if not security_scopes.scopes:
        if not ignore_scope_error:
            raise RuntimeError("Security scope missing in endpoint definition.")
    else:
        scope = security_scopes.scope_str

    scopes = scope_to_list(scope)

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token_scopes = []

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        login: str = payload.get("sub")
        token_scope: str = payload.get("scp")
        token_scopes = scope_to_list(token_scope)

        if not any(sc in token_scopes for sc in scopes):
            raise HTTPException(403, f"You do not have any of these scopes: {scope}")

        if login is None:
            raise credentials_exception
        token_data = TokenData(login=login)
    except JWTError:
        raise credentials_exception

    user = db.session.query(User).filter_by(login=token_data.login).one_or_none()
    user.scopes = token_scopes

    if user is None:
        raise credentials_exception
    return user


class CurrentUser:
    def __init__(self, ignore_scope_error=False):
        self.ignore_scope_error = ignore_scope_error

    async def __call__(self, security_scopes: SecurityScopes, token: str = Depends(oauth2_scheme)):
        return await get_current_user(security_scopes, token, self.ignore_scope_error)

@router.post("/token")
async def get_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.session.query(User).filter_by(login=form_data.username).scalar()
    if not user or user.password is None or user.password != form_data.password:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    scopes = groups_to_scopes([user.group])

    access_token = create_access_token(
        data={"sub": user.login, 'scp': list_to_scope(scopes)}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


oauth = OAuth()

oauth.register(
    name='alf',
    server_metadata_url=app_config.get('auth', 'config_url'),
    client_id=app_config.get('auth', 'client_id'),
    client_secret=app_config.get('auth', 'client_secret'),
    client_kwargs={
        'scope': 'openid email profile roles'
    }
)

def roles_to_groups(roles):
    groups = []

    rw_admin_roles = app_config.get('auth', 'rw_admin_roles').replace(" ", "").split(',')
    ro_admin_roles = app_config.get('auth', 'ro_admin_roles').replace(" ", "").split(',')
    user_roles = app_config.get('auth', 'user_roles').replace(" ", "").split(',')

    if any(r in roles for r in rw_admin_roles):
        groups += ['rw-admin']

    if any(r in roles for r in ro_admin_roles):
        groups += ['ro-admin']

    if any(r in roles for r in user_roles):
        groups += ['user']

    return groups


def groups_to_scopes(groups):
    scopes = []

    for group in groups:
        scopes += group_scopes.get(group, [])

    return list(set(scopes))


@router.get('/start')
async def login(request: Request, return_url: str = Query(...)):
    redirect_uri = url_add_parameters(request.url_for('finish'), {'return_url': return_url})

    return await oauth.alf.authorize_redirect(request, redirect_uri)


@router.get('/finish')
async def finish(request: Request, return_url: str = Query(...)):
    try:
        token = await oauth.alf.authorize_access_token(request)
        auth_user = await oauth.alf.parse_id_token(request, token)
    except OAuthError:
        raise HTTPException(400, 'Authentification Failed')

    user = session.query(User).filter_by(login=auth_user['preferred_username']).scalar()

    if user is None:
        user = User(
            login=auth_user['preferred_username'],
            name=auth_user['name'],
            email=auth_user['email'],
        )
        session.add(user)
    else:
        user.name = auth_user['name']
        user.email = auth_user['email']

    session.commit()

    groups = roles_to_groups(auth_user['roles'])
    scopes = groups_to_scopes(groups)

    access_token = create_access_token(
        data={"sub": user.login, 'scp': list_to_scope(scopes)}, expires_delta=access_token_expires
    )

    return_url = url_add_parameters(return_url, {'access_token': access_token})

    return RedirectResponse(return_url)
