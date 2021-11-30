from collections.abc import Iterable
from typing import Type, Optional, List

from lib.log import log_event
from model import User
from model.base import UUIDModel, ModelBase
from model.session import with_transaction, session

REFERENCED_OBJ = 'REFERENCED_OBJ'


def replace_ref_object(log_params, obj):
    for key, value in log_params.items():
        if value == REFERENCED_OBJ:
            log_params[key] = obj

    return log_params


def create_object(model: Type[UUIDModel],
                  processor: Optional[User] = None,
                  log_keys: List = None,
                  log_params: Optional[dict] = None,
                  **kwargs):
    classname = model.__name__

    obj = model(**kwargs)

    session.add(obj)
    session.flush()

    log_data = {
        key: obj[key]
        for key in log_keys
    } if log_keys is not None else {}

    log_params = {} if log_params is None else replace_ref_object(log_params, obj)

    log_event(f"Created {classname} with ID {obj.id}: {log_data}", creator=processor, **log_params)

    return obj


forbidden_edit_keys = ['id']


def check_equal(obj: UUIDModel, key, new_value):
    current = getattr(obj, key)

    return new_value == current


@with_transaction
def edit_object(obj: UUIDModel, processor: User, no_log: Optional[List[str]] = None,
                log_params: Optional[dict] = None, **kwargs):
    log_params = {} if log_params is None else replace_ref_object(log_params, obj)

    classname = type(obj).__name__

    for key, value in kwargs.items():
        if key in forbidden_edit_keys:
            continue

        if hasattr(obj, key) and not check_equal(obj, key, value):
            setattr(obj, key, value)

            if isinstance(value, UUIDModel):
                log_value = value.id
            elif isinstance(value, dict):
                log_value = str(value)
            elif isinstance(value, Iterable) and len(value) > 0 and isinstance(value[0], UUIDModel):
                log_value = str([v.id for v in value])
            else:
                log_value = value

            if no_log is None or key not in no_log:
                log_event(f'Edited {classname} with ID {obj.id}, set {key} = {log_value}',
                          creator=processor, **log_params)

    return obj


@with_transaction
def delete_object(obj: UUIDModel, processor: User, log_params: Optional[dict] = None,):
    log_params = {} if log_params is None else log_params

    classname = type(obj).__name__

    session.delete(obj)

    log_event(f'Deleted {classname} with id {obj.id}', processor, **log_params)

    return True
