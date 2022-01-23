from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Body, Query, Security
from fastapi_sqlalchemy import db

from api.auth import get_current_user, CurrentUser
from api.helpers import PathModelGetter, get_or_404, SuccessModel
from model import Safe, User, Location
from model.pydantic import SafeModel, SafeModelCreate, SafeModelPatch

import lib.safe

router = APIRouter(prefix="/safe", tags=["safe"])


@router.get("/", response_model=List[SafeModel],
            dependencies=[Security(CurrentUser(), scopes=['safe:read'])])
def get_safes(location_id: UUID = Query(None)):
    safes = db.session.query(Safe).filter_by(deleted=False)

    if location_id is not None:
        safes = safes.filter_by(location_id=location_id)

    return safes.all()


@router.get("/{uuid}", response_model=SafeModel,
            dependencies=[Security(CurrentUser(), scopes=['safe:read'])])
def get_safe(safe: Safe = Depends(PathModelGetter(Safe))):
    return safe


@router.post("/", response_model=SafeModel)
def create_safe(safe_create: SafeModelCreate,
                c_user: User = Security(CurrentUser(), scopes=['safe:write']),):
    args = safe_create.dict()

    args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.safe.create_safe(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=SafeModel)
def edit_safe(safe: Safe = Depends(PathModelGetter(Safe)),
              safe_patch: SafeModelPatch = Body(...),
              c_user: User = Security(CurrentUser(), scopes=['safe:write'])):
    args = safe_patch.dict(exclude_unset=True)

    if 'location_id' in args:
        args['location'] = get_or_404(Location, args.pop('location_id'))

    lock = lib.safe.edit_safe(safe, processor=c_user, **args, _commit=True)

    return lock


@router.delete("/{uuid}", response_model=SuccessModel)
def delete_safe(safe: Safe = Depends(PathModelGetter(Safe)),
                c_user: User = Security(CurrentUser(), scopes=['safe:write'])):
    lib.safe.delete_safe(safe, processor=c_user, _commit=True)

    return SuccessModel()
