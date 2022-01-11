from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import Safe, User, Location
from model.session import with_transaction


@with_transaction
def create_safe(name: str, location: Location, processor: User, note: str = None):
    return create_object(Safe,
                         log_keys=['name', 'location_id'],
                         log_params={'safe': REFERENCED_OBJ,
                                     'location': location},
                         **locals())


@with_transaction
def edit_safe(safe: Safe, processor: User, **kwargs):
    return edit_object(safe, processor, log_params={'safe': REFERENCED_OBJ,
                                                    'location': safe.location}, **kwargs)


@with_transaction
def delete_safe(safe: Safe, processor: User):
    return delete_object(safe, processor)
