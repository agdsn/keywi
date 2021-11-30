from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import Location, User


def create_location(name: str, owner: str, latitude: float, longitude: float, processor: User):
    return create_object(Location, log_keys=['name'], log_params={'location': REFERENCED_OBJ}, **locals())


def edit_location(location: Location, processor: User, **kwargs):
    return edit_object(location, processor, log_params={'location': REFERENCED_OBJ}, **kwargs)


def delete_location(location: Location, processor: User):
    return delete_object(location, processor)
