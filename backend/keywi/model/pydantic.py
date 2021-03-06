from __future__ import annotations

import inspect
from datetime import datetime
from typing import Optional, List
from uuid import UUID

from pydantic import EmailStr, constr, Field

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

# User


class UserModelBase(PydModel):
    login: constr(max_length=30, min_length=2)
    name: str
    note: Optional[str]
    role: str


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
    active_rentals: List[RentalModelShort]


# Location


class LocationModelBase(PydModel):
    name: str
    address: str = None
    latitude: float = None
    longitude: float = None
    note: Optional[str]


class LocationModelShort(PydModel):
    id: UUID
    name: str


class LocationModel(LocationModelBase):
    id: UUID
    amount_locks: int
    amount_safes: int
    deleted: bool


class LocationModelCreate(LocationModelBase):
    pass


@optional
class LocationModelPatch(LocationModelBase):
    pass


# Lock

class LockModelBase(PydModel):
    name: str
    owner: str = None
    note: Optional[str]


class LockModelShort(PydModel):
    id: UUID
    name: str
    location: LocationModelShort

class LockModel(LockModelBase):
    location: LocationModelShort
    id: UUID
    amount_keys: int
    amount_free_keys: int
    deleted: bool


class LockModelCreate(LockModelBase):
    location_id: UUID


@optional
class LockModelPatch(LockModelCreate):
    pass


# Safe

class SafeModelBase(PydModel):
    name: str
    note: Optional[str]


class SafeModel(SafeModelBase):
    id: UUID
    location: LocationModelShort
    amount_keys: int
    deleted: bool


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
    note: Optional[str]


class KeyModel(KeyModelBase):
    id: UUID
    lock: LockModelShort
    safe: SafeModelShort
    active_rental: Optional[RentalModelShort]
    checked: bool = False
    location: LocationModelShort
    deleted: bool


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
    checked: bool = False
    pass


# Rental

class RentalModelBase(PydModel):
    begin: datetime
    end: datetime = None
    allowed_by: str = Field(None, description="Name of the document that allows the user to rent this key.")
    note: Optional[str]


class RentalModel(RentalModelBase):
    id: UUID
    key: KeyModelShort
    user: UserModelShort
    issuing_user: UserModelShort
    active: bool
    end: datetime = None
    deleted: bool

class RentalModelShort(PydModel):
    id: UUID
    begin: datetime
    end: datetime = None
    user_id: UUID


class RentalModelCreate(RentalModelBase):
    begin: datetime = None
    key_id: UUID
    user_id: UUID


@optional
class RentalModelPatch(RentalModelBase):
    end: datetime = None
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
