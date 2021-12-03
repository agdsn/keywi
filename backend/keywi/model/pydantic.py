from __future__ import annotations

import inspect
from datetime import datetime
from uuid import UUID

from pydantic import EmailStr, constr

from model.base import PydModel


def optional(*fields):
    def dec(_cls):
        for field in fields:
            _cls.__fields__[field].required = False
        return _cls

    if fields and inspect.isclass(fields[0]) and issubclass(fields[0], PydModel):
        cls = fields[0]
        fields = cls.__fields__
        return dec(cls)
    return dec

# User (1/2)


class UserModelBase(PydModel):
    login: constr(max_length=30, min_length=2)
    name: str


class UserModelShort(UserModelBase):
    id: UUID


class UserModelCreate(UserModelBase):
    email: EmailStr
    password: constr(max_length=128, min_length=9)


@optional
class UserModelPatch(UserModelCreate):
    pass


class UserModel(UserModelShort):
    email: EmailStr
    active_rentals: RentalModelShort


# Location


class LocationModelBase(PydModel):
    name: str
    address: str = None
    latitude: float = None
    longitude: float = None


class LocationModelShort(PydModel):
    id: UUID
    name: str


class LocationModel(LocationModelBase):
    id: UUID
    amount_locks: int
    amount_safes: int


class LocationModelCreate(LocationModelBase):
    pass


@optional
class LocationModelPatch(LocationModelBase):
    pass


# Lock

class LockModelBase(PydModel):
    name: str
    owner: str = None


class LockModelShort(PydModel):
    id: UUID
    name: str


class LockModel(LockModelBase):
    location: LocationModelShort
    amount_keys: int
    amount_free_keys: int


class LockModelCreate(LocationModelBase):
    location_id: UUID


@optional
class LockModelPatch(LockModelCreate):
    pass


# Safe

class SafeModelBase(PydModel):
    name: str


class SafeModel(SafeModelBase):
    id: UUID
    location: LocationModelShort
    amount_keys: int


class SafeModelShort(PydModel):
    id: UUID
    name: str


class SafeModelCreate(SafeModelBase):
    location_id: UUID


@optional
class SafeModelPatch(SafeModelCreate):
    pass


# Key

class KeyModelBase(PydModel):
    number: str
    rentable: bool = False
    checked: bool = False


class KeyModel(KeyModelBase):
    id: UUID
    lock: LockModelShort
    safe: SafeModelShort
    active_rental: RentalModelShort


class KeyModelShort(PydModel):
    id: UUID
    number: str
    lock: LockModelShort
    safe: SafeModelShort


class KeyModelCreate(KeyModelBase):
    lock_id: UUID
    safe_id: UUID


@optional
class KeyModelPatch(KeyModelCreate):
    pass


# Rental

class RentalModelBase(PydModel):
    begin: datetime
    end: datetime = None
    allowed_by: str = None


class RentalModel(RentalModelBase):
    id: UUID
    key: KeyModelShort
    user: UserModelShort
    issuing_user: UserModelShort
    active: bool


class RentalModelShort(PydModel):
    id: UUID
    begin: datetime
    end: datetime = None


class RentalModelCreate(RentalModelBase):
    begin: datetime = None
    key_id: UUID
    user_id: UUID


@optional
class RentalModelPatch(RentalModelBase):
    pass


# LogEntry

class LogEntryModel(PydModel):
    timestamp: datetime
    message: str
    creator: UserModelShort

    location: LocationModelShort = None
    key: KeyModelShort = None
    user: UserModelShort = None
    lock: LockModelShort = None
    safe: SafeModelShort = None
    rental: RentalModelShort = None


UserModel.update_forward_refs()
KeyModel.update_forward_refs()
