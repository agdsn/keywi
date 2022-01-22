from typing import List

from fastapi import APIRouter, Depends, Body, Security
from fastapi_sqlalchemy import db

from api.auth import  CurrentUser
from api.helpers import PathModelGetter, SuccessModel
from model import Location, User
from model.pydantic import LocationModel, LocationModelCreate, LocationModelPatch

import lib.location

router = APIRouter(prefix="/location", tags=["location"])


@router.get("/", response_model=List[LocationModel],
            dependencies=[Security(CurrentUser(), scopes=['location:read'])])
def get_locations():
    return db.session.query(Location).all()


@router.get("/{uuid}", response_model=LocationModel,
            dependencies=[Security(CurrentUser(), scopes=['location:read'])])
def get_location(location: Location = Depends(PathModelGetter(Location))):
    return location


@router.post("/", response_model=LocationModel)
def create_location(location_create: LocationModelCreate,
                    c_user: User = Security(CurrentUser(), scopes=['location:write'])):
    args = location_create.dict()
    location = lib.location.create_location(**args, processor=c_user, _commit=True)

    return location


@router.patch("/{uuid}", response_model=LocationModel)
def edit_location(location: Location = Depends(PathModelGetter(Location)),
                  location_patch: LocationModelPatch = Body(...),
                  c_user: User = Security(CurrentUser(), scopes=['location:write'])):
    args = location_patch.dict(exclude_unset=True)

    location = lib.location.edit_location(location, processor=c_user, **args, _commit=True)

    return location


@router.delete("/{uuid}", response_model=SuccessModel)
def delete_location(location: Location = Depends(PathModelGetter(Location)),
                    c_user: User = Security(CurrentUser(), scopes=['location:write'])):
    lib.location.delete_location(location, processor=c_user, _commit=True)

    return SuccessModel()
