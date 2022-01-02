from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Body, Query
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter, get_or_404, SuccessModel
from model import Lock, User, Location
from model.pydantic import LockModel, LockModelCreate, LockModelPatch

import lib.lock

router = APIRouter(prefix="/lock", tags=["lock"])


@router.get("/", response_model=List[LockModel])
def get_locks(location_id: UUID = Query(None)):
    locks = db.session.query(Lock)

    if location_id is not None:
        locks = locks.filter_by(location_id=location_id)

    return locks.all()


@router.get("/{uuid}", response_model=LockModel)
def get_lock(lock: Lock = Depends(PathModelGetter(Lock))):
    return lock


@router.post("/", response_model=LockModel)
def create_lock(lock_create: LockModelCreate,
                c_user: User = Depends(get_current_user)):
    args = lock_create.dict()

    args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.lock.create_lock(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=LockModel)
def edit_lock(lock: Lock = Depends(PathModelGetter(Lock)),
              lock_patch: LockModelPatch = Body(...),
              c_user: User = Depends(get_current_user)):
    args = lock_patch.dict(exclude_unset=True)

    if 'location_id' in args:
        args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.lock.edit_lock(lock, processor=c_user, **args, _commit=True)

    return lock


@router.delete("/{uuid}", response_model=SuccessModel)
def delete_lock(lock: Lock = Depends(PathModelGetter(Lock)),
                c_user: User = Depends(get_current_user)):
    lib.lock.delete_lock(lock, processor=c_user, _commit=True)

    return SuccessModel
