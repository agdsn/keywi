from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Body, Query, Security
from fastapi_sqlalchemy import db

from api.auth import CurrentUser
from api.helpers import PathModelGetter, get_or_404, SuccessModel
from model import Key, User, Lock, Safe
from model.pydantic import KeyModel, KeyModelCreate, KeyModelPatch

import lib.key

router = APIRouter(prefix="/key", tags=["key"])


@router.get("/", response_model=List[KeyModel],
            dependencies=[Security(CurrentUser(), scopes=['key:read'])])
def get_keys(safe_id: UUID = Query(None), lock_id: UUID = Query(None)):
    keys = db.session.query(Key)

    if safe_id is not None:
        keys = keys.filter_by(safe_id=safe_id)

    if lock_id is not None:
        keys = keys.filter_by(lock_id=lock_id)

    return keys.all()


@router.get("/{uuid}", response_model=KeyModel, dependencies=[Security(CurrentUser(), scopes=['key:read'])])
def get_key(key: Key = Depends(PathModelGetter(Key))):
    return key


@router.post("/", response_model=KeyModel)
def create_key(key_create: KeyModelCreate,
               c_user: User = Security(CurrentUser(), scopes=['key:write'])):
    args = key_create.dict()

    args['lock'] = get_or_404(Lock, args.pop('lock_id'))
    args['safe'] = get_or_404(Safe, args.pop('safe_id'))

    lock = lib.key.create_key(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=KeyModel)
def edit_key(key: Key = Depends(PathModelGetter(Key)),
             key_patch: KeyModelPatch = Body(...),
             c_user: User = Security(CurrentUser(), scopes=['key:write'])):
    args = key_patch.dict(exclude_unset=True)

    if 'lock' in args:
        args['lock'] = get_or_404(Lock, args.pop('lock_id'))

    if 'safe' in args:
        args['safe'] = get_or_404(Safe, args.pop('safe_id'))

    key = lib.key.edit_key(key, processor=c_user, **args, _commit=True)

    return key


@router.delete("/{uuid}", response_model=SuccessModel,)
def delete_key(key: Key = Depends(PathModelGetter(Key)),
               c_user: User = Security(CurrentUser(), scopes=['key:write'])):
    lib.key.delete_key(key, processor=c_user, _commit=True)

    return SuccessModel
