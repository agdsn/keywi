from model import User, Location, Lock, Safe, Key, Rental, LogEntry
from model.session import with_transaction, session


@with_transaction
def init_data():
    admin = User(
        login='admin',
        name="Admin",
        email="root@lists.agdsn.de",
        role="rw-admin",
        password='admin',
    )
    session.add(admin)

    user = User(
        login='user',
        name="User",
        email="user@test.de",
        role="user",
        password='user',
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
