from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends, Body, Query, HTTPException
from fastapi_sqlalchemy import db

from api.auth import get_current_user
from api.helpers import PathModelGetter, get_or_404, SuccessModel
from model import Rental, User, Key, utcnow
from model.pydantic import RentalModel, RentalModelCreate, RentalModelPatch

import lib.rental

router = APIRouter(prefix="/rental", tags=["rental"])


@router.get("/", response_model=List[RentalModel])
def get_rentals(key_id: UUID = Query(None),
                user_id: UUID = Query(None),
                issuing_user_id: UUID = Query(None),
                ):
    rentals = db.session.query(Rental)

    if key_id is not None:
        rentals = rentals.filter_by(key_id=key_id)

    if user_id is not None:
        rentals = rentals.filter_by(user_id=user_id)

    if issuing_user_id is not None:
        rentals = rentals.filter_by(issuing_user_id=issuing_user_id)

    return rentals.all()


@router.get("/{uuid}", response_model=RentalModel)
def get_rental(rental: Rental = Depends(PathModelGetter(Rental))):
    return rental


@router.post("/", response_model=RentalModel)
def create_rental(rental_create: RentalModelCreate,
                  c_user: User = Depends(get_current_user)):
    args = rental_create.dict()

    args['user'] = get_or_404(User, args.pop('user_id'))
    args['key'] = get_or_404(Key, args.pop('key_id'))

    try:
        rental = lib.rental.create_rental(**args, issuing_user=c_user, processor=c_user, _commit=True)
    except lib.rental.RentalRangeOverlapException as e:
        raise HTTPException(400, str(e))

    return rental


@router.patch("/{uuid}", response_model=RentalModel)
def edit_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                rental_patch: RentalModelPatch = Body(...),
                c_user: User = Depends(get_current_user)):
    args = rental_patch.dict(exclude_unset=True)

    try:
        rental = lib.rental.edit_rental(rental, processor=c_user, **args, _commit=True)
    except lib.rental.RentalRangeOverlapException as e:
        raise HTTPException(400, str(e))

    return rental


@router.delete("/{uuid}", response_model=SuccessModel)
def delete_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                  c_user: User = Depends(get_current_user)):
    lib.rental.delete_rental(rental, processor=c_user, _commit=True)

    return SuccessModel()


@router.post("/{uuid}/end", response_model=RentalModel)
def end_rental(rental: Rental = Depends(PathModelGetter(Rental)),
                  c_user: User = Depends(get_current_user)):
    rental = lib.rental.edit_rental(rental, processor=c_user, end=utcnow(), _commit=True)

    return rental
