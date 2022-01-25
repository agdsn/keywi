import uuid

from pydantic import BaseModel
from sqlalchemy import Column, func, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import declarative_base

ModelBase = declarative_base()

class UUIDModel(ModelBase):
    """
    Abstract base class for database models with an UUID primary column,
    named ``id``.
    """

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.uuid_generate_v4())
    deleted = Column(Boolean, nullable=False, server_default='False')


class PydModel(BaseModel):
    class Config:
        orm_mode = True
