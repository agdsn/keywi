from http.client import HTTPException
from typing import Type
from uuid import UUID

from fastapi import FastAPI, Path
from fastapi.routing import APIRoute

from model import UUIDModel
from model.base import ModelBase


def to_camel_case(snake_str):
    components = snake_str.split('_')
    # We capitalize the first letter of each component except the first one
    # with the 'title' method and join them together.
    return components[0] + ''.join(x.title() for x in components[1:])


def use_route_names_as_operation_ids(app: FastAPI) -> None:
    """
    Simplify operation IDs so that generated API clients have simpler function
    names.

    Should be called only after all routes have been added.
    """
    for route in app.routes:
        if isinstance(route, APIRoute):
            route.operation_id = '{}_{}'.format('_'.join(route.tags), to_camel_case(route.name))


def is_valid_uuid(uuid_to_test, version=4):
    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


class PathModelGetter:
    model = None

    def __init__(self, model: Type[UUIDModel]):
        self.model = model

    def __call__(self, uuid=Path(..., description="The UUID of the referenced object.")):
        obj = None

        if is_valid_uuid(uuid):
            obj = self.model.q.get(uuid)

        if obj is None:
            raise HTTPException(404, f"{self.model.__name__} with UUID {uuid} not found!")

        return obj


def get_or_404(model: Type[ModelBase], ident: any):
    obj = model.q.get(ident)

    if obj is None:
        raise HTTPException(404, f'{model.__name__} with identifier {ident} not found!')

    return obj
