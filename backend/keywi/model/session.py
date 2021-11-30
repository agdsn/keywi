from fastapi_sqlalchemy import db
import wrapt

scoped_session = None


class SessionWrapper:
    def __getattr__(self, name):
        if scoped_session is not None:
            return getattr(scoped_session, name)

        return getattr(db.session, name)


session = SessionWrapper()


@wrapt.decorator
def with_transaction(wrapped, instance=None, args=[], kwargs={}):
    transaction = session.begin(subtransactions=True)

    try:
        commit = kwargs.pop('_commit', False)

        rv = wrapped(*args, **kwargs)
        transaction.commit()

        if commit:
            session.commit()

        return rv
    except:
        transaction.rollback()
        raise


def set_scoped_session(s):
    global scoped_session

    scoped_session = s


def remove_scoped_session():
    global scoped_session

    scoped_session = None
