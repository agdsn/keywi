from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter, get_or_404
from model import Safe, User, Location
from model.pydantic import SafeModel, SafeModelCreate, SafeModelPatch

import lib.safe

router = APIRouter(prefix="/safe", tags=["safe"])


@router.get("/", response_model=List[SafeModel])
def get_safes():
    return db.session.query(Safe).all()


@router.get("/{uuid}", response_model=SafeModel)
def get_safe(safe: Safe = Depends(PathModelGetter(Safe))):
    return safe


@router.post("/", response_model=SafeModel)
def create_safe(safe_create: SafeModelCreate,
                c_user: User = Depends(get_current_user)):
    args = safe_create.dict()

    args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.safe.create_safe(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=SafeModel)
def edit_safe(safe: Safe = Depends(PathModelGetter(Safe)),
              safe_patch: SafeModelPatch = Body(...),
              c_user: User = Depends(get_current_user)):
    args = safe_patch.dict(exclude_unset=True)

    if 'location_id' in args:
        args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.safe.edit_safe(safe, processor=c_user, **args, _commit=True)

    return lock


@router.delete("/{uuid}", response_model=SafeModel)
def delete_safe(safe: Safe = Depends(PathModelGetter(Safe)),
                c_user: User = Depends(get_current_user)):
    return lib.safe.delete_safe(safe, processor=c_user, _commit=True)
