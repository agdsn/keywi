from lib.crud import create_object, REFERENCED_OBJ, edit_object, delete_object
from model import Lock, User, Location


def create_lock(name: str, owner: str, location: Location, processor: User):
    return create_object(Lock,
                         log_keys=['name', 'owner', 'location_id'],
                         log_params={'lock': REFERENCED_OBJ, 'location': location},
                         **locals())


def edit_lock(lock: Lock, processor: User, **kwargs):
    return edit_object(lock, processor, log_params={'lock': REFERENCED_OBJ, 'location': lock.location}, **kwargs)


def delete_lock(lock: Lock, processor: User):
    return delete_object(lock, processor, log_params={'location': lock.location})
