from fastapi import Depends, HTTPException, status, APIRouter
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi_sqlalchemy import db

from model import User

router = APIRouter(prefix="/auth", tags=["auth"])

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: str = Depends(oauth2_scheme)) -> User:
    user = db.session.query(User).filter_by(login=token).one_or_none()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.session.query(User).filter_by(login=form_data.username).scalar()
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    return {"access_token": user.login, "token_type": "bearer"}


