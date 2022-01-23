from typing import List

from fastapi import APIRouter, Depends, Security
from fastapi_sqlalchemy import db

from api.auth import get_current_user, CurrentUser
from api.helpers import PathModelGetter, raise_permission_error
from model import User
from model.pydantic import UserModel

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[UserModel])
def get_users(c_user: User = Security(CurrentUser(), scopes=['user:read', 'user:self:read'])):
    users = db.session.query(User)

    if 'user:read' not in c_user.scopes:
        users = users.filter_by(id=c_user.id)

    return users.all()


@router.get("/current", response_model=UserModel)
def get_current(c_user: User = Security(CurrentUser(), scopes=['user:read', 'user:self:read'])):
    return c_user


@router.get("/{uuid}", response_model=UserModel)
def get_user(user: User = Depends(PathModelGetter(User)),
             c_user: User = Security(CurrentUser(), scopes=['user:read', 'user:self:read'])):
    if c_user != user and 'user:read' not in c_user.scopes:
        raise_permission_error()

    return user
