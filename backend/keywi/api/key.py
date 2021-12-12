from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter, get_or_404, SuccessModel
from model import Key, User, Lock, Safe
from model.pydantic import KeyModel, KeyModelCreate, KeyModelPatch

import lib.key

router = APIRouter(prefix="/key", tags=["key"])


@router.get("/", response_model=List[KeyModel])
def get_keys():
    return db.session.query(Key).all()


@router.get("/{uuid}", response_model=KeyModel)
def get_key(key: Key = Depends(PathModelGetter(Key))):
    return key


@router.post("/", response_model=KeyModel)
def create_key(key_create: KeyModelCreate,
               c_user: User = Depends(get_current_user)):
    args = key_create.dict()

    args['lock'] = get_or_404(Lock, args.pop('lock_id'))
    args['safe'] = get_or_404(Safe, args.pop('safe_id'))

    lock = lib.key.create_key(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=KeyModel)
def edit_key(key: Key = Depends(PathModelGetter(Key)),
             key_patch: KeyModelPatch = Body(...),
             c_user: User = Depends(get_current_user)):
    args = key_patch.dict(exclude_unset=True)

    if 'lock' in args:
        args['lock'] = get_or_404(Lock, args.pop('lock_id'))

    if 'safe' in args:
        args['safe'] = get_or_404(Safe, args.pop('safe_id'))

    key = lib.key.edit_key(key, processor=c_user, **args, _commit=True)

    return key


@router.delete("/{uuid}", response_model=SuccessModel,)
def delete_key(key: Key = Depends(PathModelGetter(Key)),
               c_user: User = Depends(get_current_user)):
    lib.key.delete_key(key, processor=c_user, _commit=True)

    return SuccessModel
