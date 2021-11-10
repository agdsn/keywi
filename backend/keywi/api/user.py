from fastapi import APIRouter
from fastapi_sqlalchemy import db

from model import User

router = APIRouter(prefix="/user")

@router.get("/")
async def root():
    user = User(login="test", name="Test Hans", email="Test@123.de")

    db.session.add(user)
    db.session.commit()

    return {"message": "Hello World"}
