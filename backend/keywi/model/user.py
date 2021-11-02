from sqlalchemy import String, Column

from model.base import UUIDModel


class User(UUIDModel):
    name = Column(String)
