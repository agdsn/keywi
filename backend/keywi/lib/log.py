from fastapi_sqlalchemy import db

from model import User, LogEntry


def log_event(message: str, creator: User = None, **log_params):
    """
    This method will create a new LogEntry.
    """
    with db():
        le = LogEntry(
            message=message,
            creator=creator,
            **log_params,
        )

        db.session.add(le)

    return le
