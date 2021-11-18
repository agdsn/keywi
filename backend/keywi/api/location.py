from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import Location
from model.pydantic import LocationModel, LocationModelCreate, LocationModelPatch

router = APIRouter(prefix="/location", tags=["location"])


@router.get("/", response_model=List[LocationModel])
def get_locations():
    return db.session.query(Location).all()


@router.get("/{uuid}", response_model=LocationModel)
def get_location(location: Location = Depends(PathModelGetter(Location))):
    return location


@router.post("/", response_model=LocationModel)
def create_location(location_create: LocationModelCreate):
    pass


@router.patch("/{uuid}", response_model=LocationModel)
def edit_location(location: Location = Depends(PathModelGetter(Location)),
                  location_patch: LocationModelPatch = Body(...)):
    pass


@router.delete("/{uuid}", response_model=LocationModel)
def delete_location(location: Location = Depends(PathModelGetter(Location))):
    pass
