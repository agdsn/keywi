from model import User, LogEntry, Lock, Location
from model.session import session


def log_event(message: str,
              creator: User = None,
              **kwargs):
    """
    This method will create a new LogEntry.
    """
    le = LogEntry(
        message=message,
        creator=creator,
        **kwargs,
    )

    session.add(le)

    return le
