from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import Lock
from model.pydantic import LockModel, LockModelCreate, LockModelPatch

router = APIRouter(prefix="/lock", tags=["lock"])


@router.get("/", response_model=List[LockModel])
def get_locks():
    return db.session.query(Lock).all()


@router.get("/{uuid}", response_model=LockModel)
def get_lock(lock: Lock = Depends(PathModelGetter(Lock))):
    return lock


@router.post("/", response_model=LockModel)
def create_lock(lock_create: LockModelCreate):
    pass


@router.patch("/{uuid}", response_model=LockModel)
def edit_lock(lock: Lock = Depends(PathModelGetter(Lock)),
              lock_patch: LockModelPatch = Body(...)):
    pass


@router.delete("/{uuid}", response_model=LockModel)
def delete_lock(lock: Lock = Depends(PathModelGetter(Lock))):
    pass
