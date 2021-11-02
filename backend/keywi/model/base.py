import re
import uuid

from sqlalchemy import Column, func
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import as_declarative, declared_attr


@as_declarative()
class ModelBase(object):
    """Base class for all database models."""

    @declared_attr
    def __tablename__(cls):
        """Autogenerate the tablename for the mapped objects."""
        return cls._to_snake_case(cls.__name__)

    @staticmethod
    def _to_snake_case(name):
        name = re.sub(r"([A-Z]+)([A-Z][a-z])", r'\1_\2', name)
        name = re.sub(r"([a-z\d])([A-Z])", r'\1_\2', name)
        return name.lower()

    def __repr__(self):
        return "{0}.{1}({2})".format(
            self.__module__, self.__class__.__name__,
            ", ".join("{0}={1!r}".format(key, getattr(self, key, "<unknown>"))
                      for key in self.__mapper__.columns.keys()))

class UUIDModel(ModelBase):
    """
    Abstract base class for database models with an UUID primary column,
    named ``id``.
    """

    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, server_default=func.uuid_generate_v4())
