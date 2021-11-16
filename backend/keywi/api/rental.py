from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.helpers import PathModelGetter
from model import Rental
from model.pydantic import RentalModel, RentalModelCreate, RentalModelPatch

router = APIRouter(prefix="/rental", tags=["rental"])


@router.get("/", response_model=List[RentalModel])
def get_rentals():
    return db.session.query(Rental).all()


@router.get("/{uuid}", response_model=RentalModel)
def get_rental(rental: Rental = Depends(PathModelGetter(Rental))):
    return rental


@router.post("/", response_model=RentalModel)
def create_rental(rental_create: RentalModelCreate):
    pass


@router.patch("/{uuid}", response_model=RentalModel)
def edit_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                  rental_patch: RentalModelPatch = Body(...)):
    pass


@router.delete("/{uuid}", response_model=RentalModel)
def delete_rental(rental: Rental = Depends(PathModelGetter(Rental))):
    pass
