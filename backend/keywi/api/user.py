from typing import List

from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter
from model import User
from model.pydantic import UserModel

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[UserModel])
def get_users():
    return db.session.query(User).all()


@router.get("/current", response_model=UserModel)
def get_current(c_user: User = Depends(get_current_user)):
    return c_user


@router.get("/{uuid}", response_model=UserModel)
def get_user(user: User = Depends(PathModelGetter(User))):
    return user
