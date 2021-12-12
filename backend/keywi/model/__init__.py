from sqlalchemy import String, Column, ForeignKey, Boolean, DateTime, CheckConstraint, func, Float, or_, select, and_
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship, backref
from sqlalchemy_utils import EmailType, PasswordType

from model.base import UUIDModel
from model.time import utcnow


class User(UUIDModel):
    __tablename__ = "user"

    login = Column(String, nullable=False, unique=True)
    name = Column(String, nullable=False)
    email = Column(EmailType, nullable=False)
    password = Column(PasswordType(schemes=['pbkdf2_sha512']))

    active_rentals = relationship("Rental", primaryjoin="and_(Rental.user_id == User.id,"
                                                        "     Rental.active)",)


class Location(UUIDModel):
    __tablename__ = "location"

    name = Column(String, nullable=False)
    address = Column(String)
    latitude = Column(Float)
    longitude = Column(Float)

    @property
    def amount_locks(self):
        return len(self.locks)

    @property
    def amount_safes(self):
        return len(self.safes)


class Lock(UUIDModel):
    __tablename__ = "lock"

    name = Column(String, nullable=False)
    owner = Column(String, nullable=True, comment="The organization/person who owns the lock.")
    location_id = Column(ForeignKey("location.id", ondelete="CASCADE"), nullable=False)

    location = relationship("Location", backref=backref("locks"))

    free_keys = relationship("Key", primaryjoin="and_(Key.lock_id == Lock.id,"
                                                "     Key.free)")

    @property
    def amount_keys(self):
        return len(self.keys)

    @property
    def amount_free_keys(self):
        return len(self.free_keys)


class Safe(UUIDModel):
    __tablename__ = "safe"

    name = Column(String, nullable=False)
    location_id = Column(ForeignKey("location.id", ondelete="CASCADE"), nullable=False)

    location = relationship("Location", backref=backref("safes"))

    @property
    def amount_keys(self):
        return len(self.keys)


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

    active_rental = relationship("Rental", uselist=False,
                                 primaryjoin="and_(Rental.key_id == Key.id, Rental.active)")

    @hybrid_property
    def free(self):
        return self.active_rental is None

    @free.expression
    def free(self):
        return select(Rental.id).select_from(Rental).where(and_(Rental.active, Rental.key_id == self.id)).scalar_subquery().is_(None)

    @property
    def location(self):
        return self.lock.location

class Rental(UUIDModel):
    __tablename__ = "rental"
    __table_args__ = (
        CheckConstraint('("end" is null) or ("end" >= "begin")'),
    )

    begin = Column(DateTime(timezone=True), nullable=False, server_default=func.now())
    end = Column(DateTime(timezone=True), nullable=True)
    allowed_by = Column(String, comment="Name of the document that allows the user to rent this key.")
    key_id = Column(ForeignKey("key.id", ondelete="CASCADE"), nullable=False)
    user_id = Column(ForeignKey("user.id", ondelete="CASCADE"), nullable=False)
    issuing_user_id = Column(ForeignKey("user.id", ondelete="SET NULL"), nullable=True)

    key = relationship("Key", backref=backref("rentals", overlaps="active_rental"), overlaps="active_rental")
    user = relationship("User", backref=backref("rentals", overlaps="active_rentals"), primaryjoin="Rental.user_id == User.id",
                        overlaps="active_rentals")
    issuing_user = relationship("User", backref=backref("issued_rentals"), primaryjoin="Rental.issuing_user_id == User.id")

    @hybrid_property
    def active(self):
        return self.end is None or self.end > utcnow()

    @active.expression
    def active(self):
        return or_(self.end.is_(None), self.end > func.now())


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
    rental_id = Column(ForeignKey("rental.id", ondelete="CASCADE"))

    creator = relationship("User", backref=backref("activity_log_entries"), primaryjoin="LogEntry.creator_id == User.id")

    location = relationship("Location", backref=backref("log_entries"))
    key = relationship("Key", backref=backref("log_entries"))
    user = relationship("User", backref=backref("log_entries"), primaryjoin="LogEntry.user_id == User.id")
    lock = relationship("Lock", backref=backref("log_entries"))
    safe = relationship("Safe", backref=backref("log_entries"))
    rental = relationship("Rental", backref=backref("log_entries"))
