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

# User

class UserModel(PydModel):
    id: UUID
    login: constr(max_length=30, min_length=2)
    name: str
    email: EmailStr


# Location

class LocationModelBase(PydModel):
    name: str
    address: str = None
    latitude: float = None
    longitude: float = None

class LocationModel(LocationModelBase):
    id: UUID

class LocationModelCreate(LocationModelBase):
    pass

@optional
class LocationModelPatch(LocationModelBase):
    pass


# Lock

class LockModelBase(PydModel):
    name: str
    owner: str = None


class LockModel(LockModelBase):
    id: UUID
    location: LocationModel

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
    location: LocationModel

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
    lock: LockModel
    safe: SafeModel

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
    key: KeyModel
    user: UserModel
    issuing_user: UserModel

class RentalModelCreate(RentalModelBase):
    begin: datetime = None
    key_id: KeyModel
    user_id: UserModel

@optional
class RentalModelPatch(RentalModelCreate):
    pass


# LogEntry

class LogEntryModel(PydModel):
    timestamp: datetime
    message: str
    creator: UserModel

    location: LocationModel = None
    key: KeyModel = None
    user: UserModel = None
    lock: LockModel = None
    safe: SafeModel = None
    rental: RentalModel = None
