from lib.crud import create_object, REFERENCED_OBJ, edit_object, delete_object
from model import Lock, User, Location
from model.session import with_transaction


@with_transaction
def create_lock(name: str, owner: str, location: Location, processor: User, note: str = None):
    return create_object(Lock,
                         log_keys=['name', 'owner', 'location_id'],
                         log_params={'lock': REFERENCED_OBJ, 'location': location},
                         **locals())


@with_transaction
def edit_lock(lock: Lock, processor: User, **kwargs):
    return edit_object(lock, processor, log_params={'lock': REFERENCED_OBJ, 'location': lock.location}, **kwargs)


@with_transaction
def delete_lock(lock: Lock, processor: User):
    return delete_object(lock, processor, childs=['keys'],
                         log_params={'location': lock.location,
                                     'lock': REFERENCED_OBJ,})
