from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import Location, User
from model.session import with_transaction


@with_transaction
def create_location(name: str, address: str, latitude: float, longitude: float, processor: User, note: str = None):
    return create_object(Location, log_keys=['name'], log_params={'location': REFERENCED_OBJ}, **locals())


@with_transaction
def edit_location(location: Location, processor: User, **kwargs):
    return edit_object(location, processor, log_params={'location': REFERENCED_OBJ}, **kwargs)


@with_transaction
def delete_location(location: Location, processor: User):
    return delete_object(location, processor, childs=['locks', 'keys'],
                         log_params={'location': REFERENCED_OBJ})
