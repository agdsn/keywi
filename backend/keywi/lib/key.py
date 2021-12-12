from lib.crud import create_object, REFERENCED_OBJ, edit_object, delete_object
from model import Key, Lock, User, Safe
from model.session import with_transaction


@with_transaction
def create_key(number: str, lock: Lock, safe: Safe, processor: User, rentable: bool = False, checked: bool = False):
    return create_object(Key,
                         log_keys=['number', 'lock_id', 'safe_id'],
                         log_params={'key': REFERENCED_OBJ, 'safe': safe},
                         **locals())


@with_transaction
def edit_key(key: Key, processor: User, **kwargs):
    return edit_object(key, processor, log_params={'key': REFERENCED_OBJ, 'safe': key.safe, 'lock': key.lock}, **kwargs)


@with_transaction
def delete_key(key: Key, processor: User):
    return delete_object(key, processor, log_params={'safe': key.safe, 'lock': key.lock})
