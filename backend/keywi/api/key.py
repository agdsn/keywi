from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import Key
from model.pydantic import KeyModel, KeyModelCreate, KeyModelPatch

router = APIRouter(prefix="/key", tags=["key"])


@router.get("/", response_model=List[KeyModel])
def get_keys():
    return db.session.query(Key).all()


@router.get("/{uuid}", response_model=KeyModel)
def get_key(key: Key = Depends(PathModelGetter(Key))):
    return key


@router.post("/", response_model=KeyModel)
def create_key(key_create: KeyModelCreate):
    pass


@router.patch("/{uuid}", response_model=KeyModel)
def edit_key(key: Key = Depends(PathModelGetter(Key)),
             key_patch: KeyModelPatch = Body(...)):
    pass


@router.delete("/{uuid}", response_model=KeyModel)
def delete_key(key: Key = Depends(PathModelGetter(Key))):
    pass
