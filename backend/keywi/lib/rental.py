from datetime import datetime

from lib.crud import create_object, REFERENCED_OBJ, delete_object, edit_object
from model import Rental, User, Location, Key
from model.session import with_transaction


@with_transaction
def create_rental(key: Key, user: User, issuing_user: User, processor: User, begin: datetime = None,
                  allowed_by: str = None):
    return create_object(Rental,
                         log_keys=['key_id', 'user_id', 'issuing_user_id', 'begin', 'allowed_by'],
                         log_params={'rental': REFERENCED_OBJ,
                                     'key': key,
                                     'user': user},
                         **locals())


@with_transaction
def edit_rental(rental: Rental, processor: User, **kwargs):
    return edit_object(rental, processor, log_params={'rental': REFERENCED_OBJ,
                                                      'key': rental.key,
                                                      'user': rental.user}, **kwargs)


@with_transaction
def delete_rental(rental: Rental, processor: User):
    return delete_object(rental, processor)
