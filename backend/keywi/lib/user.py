from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import User
from model.session import with_transaction


@with_transaction
def create_user(name: str, login: str, email: str, password: str, processor: User, note: str = None):
    return create_object(User,
                         log_keys=['email', 'note'],
                         log_params={'user': REFERENCED_OBJ},
                         **locals())


@with_transaction
def edit_user(user: User, processor: User, **kwargs):
    return edit_object(user, processor, log_params={'user': REFERENCED_OBJ}, **kwargs,
                       no_log=['password'])


@with_transaction
def delete_user(user: User, processor: User):
    return delete_object(user, processor)
