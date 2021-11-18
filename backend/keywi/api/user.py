from typing import List

from fastapi import APIRouter, Depends
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import User
from model.pydantic import UserModel

router = APIRouter(prefix="/user", tags=["user"])


@router.get("/", response_model=List[UserModel])
def get_users():
    return db.session.query(User).all()


@router.get("/{uuid}", response_model=UserModel)
def get_user(user: User = Depends(PathModelGetter(User))):
    return user
