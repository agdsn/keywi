import uuid

from pydantic import BaseModel
from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

ModelBase = declarative_base()

class UUIDModel(ModelBase):
    """
    Abstract base class for database models with an UUID primary column,
    named ``id``.
    """

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.uuid_generate_v4())


class PydModel(BaseModel):
    class Config:
        orm_mode = True
