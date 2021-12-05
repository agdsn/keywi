from typing import List

from fastapi import APIRouter, Depends, Body
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter, get_or_404
from model import Rental, User, Key
from model.pydantic import RentalModel, RentalModelCreate, RentalModelPatch

import lib.rental

router = APIRouter(prefix="/rental", tags=["rental"])


@router.get("/", response_model=List[RentalModel])
def get_rentals():
    return db.session.query(Rental).all()


@router.get("/{uuid}", response_model=RentalModel)
def get_rental(rental: Rental = Depends(PathModelGetter(Rental))):
    return rental


@router.post("/", response_model=RentalModel)
def create_rental(rental_create: RentalModelCreate,
                  c_user: User = Depends(get_current_user)):
    args = rental_create.dict()

    args['user'] = get_or_404(User, args.pop('user_id'))
    args['key'] = get_or_404(Key, args.pop('key_id'))

    lock = lib.rental.create_rental(**args, processor=c_user, _commit=True)

    return lock


@router.patch("/{uuid}", response_model=RentalModel)
def edit_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                rental_patch: RentalModelPatch = Body(...),
                c_user: User = Depends(get_current_user)):
    args = rental_patch.dict(exclude_unset=True)

    lock = lib.rental.edit_rental(rental, processor=c_user, **args, _commit=True)

    return lock


@router.delete("/{uuid}", response_model=RentalModel)
def delete_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                  c_user: User = Depends(get_current_user)):
    return lib.rental.delete_rental(rental, processor=c_user, _commit=True)
