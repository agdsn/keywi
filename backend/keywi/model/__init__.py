from sqlalchemy import String, Column, ForeignKey, Boolean, DateTime, CheckConstraint, func, Float
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import EmailType

from model.base import UUIDModel


class User(UUIDModel):
    __tablename__ = "user"

    login = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False)


class Location(UUIDModel):
    __tablename__ = "location"

    name = Column(String, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)


class Lock(UUIDModel):
    __tablename__ = "lock"

    name = Column(String, nullable=False)
    owner = Column(String, nullable=True, comment="The organization/person who owns the lock.")
    location_id = Column(ForeignKey("location.id", ondelete="CASCADE"), nullable=False)

    location = relationship("Location", backref=backref("locks"))


class Safe(UUIDModel):
    __tablename__ = "safe"

    name = Column(String, nullable=False)
    location_id = Column(ForeignKey("location.id", ondelete="CASCADE"), nullable=False)

    location = relationship("Location", backref=backref("safes"))


class Key(UUIDModel):
    __tablename__ = "key"

    number = Column(String, nullable=False)
    rentable = Column(Boolean, nullable=False, server_default="False", comment="Is available for long-time rental.")
    lock_id = Column(ForeignKey("lock.id", ondelete="CASCADE"), nullable=False)
    safe_id = Column(ForeignKey("safe.id", ondelete="SET NULL"))
    checked = Column(Boolean, nullable=False, server_default="False",
                     comment="Has been checked to be in the correct location. Reset all to false for a new inventory.")

    lock = relationship("Lock", backref=backref("keys"))
    safe = relationship("Safe", backref=backref("keys"))


class Rental(UUIDModel):
    __tablename__ = "rental"
    __table_args__ = (
        CheckConstraint('("end" is null) or ("end" >= "begin")'),
    )

    begin = Column(DateTime(timezone=True), nullable=False)
    end = Column(DateTime(timezone=True), nullable=True)
    allowed_by = Column(String, comment="Name of the document that allows the user to rent this key.")
    key_id = Column(ForeignKey("key.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    issuing_user_id = Column(ForeignKey("user.id", ondelete="SET NULL"), nullable=True)

    key = relationship("Key", backref=backref("rentals"))
    user = relationship("User", backref=backref("rentals"), primaryjoin="Rental.user_id == User.id")
    issuing_user = relationship("User", backref=backref("issued_rentals"), primaryjoin="Rental.issuing_user_id == User.id")


class LogEntry(UUIDModel):
    __tablename__ = "log_entry"

    timestamp = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    message = Column(String, nullable=False)
    creator_id = Column(ForeignKey("user.id", ondelete="SET NULL"), nullable=True)

    location_id = Column(ForeignKey("location.id", ondelete="CASCADE"))
    key_id = Column(ForeignKey("key.id", ondelete="CASCADE"))
    user_id = Column(ForeignKey("user.id", ondelete="CASCADE"))
    lock_id = Column(ForeignKey("lock.id", ondelete="CASCADE"))
    safe_id = Column(ForeignKey("safe.id", ondelete="CASCADE"))

    creator = relationship("User", backref=backref("activity_log_entries"), primaryjoin="LogEntry.creator_id == User.id")

    location = relationship("Location", backref=backref("log_entries"))
    key = relationship("Key", backref=backref("log_entries"))
    user = relationship("User", backref=backref("log_entries"), primaryjoin="LogEntry.user_id == User.id")
    lock = relationship("Lock", backref=backref("log_entries"))
    safe = relationship("Safe", backref=backref("log_entries"))
