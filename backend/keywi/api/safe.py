from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import Safe
from model.pydantic import SafeModel, SafeModelCreate, SafeModelPatch

router = APIRouter(prefix="/safe", tags=["safe"])


@router.get("/", response_model=List[SafeModel])
def get_safes():
    return db.session.query(Safe).all()


@router.get("/{uuid}", response_model=SafeModel)
def get_safe(safe: Safe = Depends(PathModelGetter(Safe))):
    return safe


@router.post("/", response_model=SafeModel)
def create_safe(safe_create: SafeModelCreate):
    pass


@router.patch("/{uuid}", response_model=SafeModel)
def edit_safe(safe: Safe = Depends(PathModelGetter(Safe)),
                  safe_patch: SafeModelPatch = Body(...)):
    pass


@router.delete("/{uuid}", response_model=SafeModel)
def delete_safe(safe: Safe = Depends(PathModelGetter(Safe))):
    pass
