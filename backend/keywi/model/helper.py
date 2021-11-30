from model import User, Location, Lock, Safe, Key, Rental, LogEntry
from model.session import with_transaction, session


@with_transaction
def init_data():
    user = User(
        login='test',
        name="Test User",
        email="test@test.test"
    )
    session.add(user)

    location = Location(
        name="Test Location",
        address="Test Address",
        latitude="1",
        longitude="2",
    )
    session.add(location)

    lock = Lock(
        name="Test Lock",
        owner="Test Company",
        location=location,
    )
    session.add(lock)

    safe = Safe(
        name="Test Safe",
        location=location
    )
    session.add(safe)

    key = Key(
        number="T1",
        rentable=True,
        lock=lock,
        safe=safe,
    )
    session.add(key)

    rental = Rental(
        allowed_by="Test Document",
        key=key,
        user=user,
        issuing_user=user,
    )
    session.add(rental)

    log_entry = LogEntry(
        message="Test log message",
        creator=user,
        location=location,
        key=key,
        user=user,
        lock=lock,
        safe=safe,
    )
    session.add(log_entry)
