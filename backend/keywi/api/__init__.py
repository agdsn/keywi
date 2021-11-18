from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

import model, model.base
from api import user, safe, rental, log, lock, location, key
from api.helpers import use_route_names_as_operation_ids

from lib.app_config import app_config


app = FastAPI(title="Keywi", version="0.0.1")
app.add_middleware(DBSessionMiddleware, db_url=app_config.get('database', 'url'))

with db():
    model.base.ModelBase.metadata.create_all(db.session.get_bind())

app.include_router(key.router)
app.include_router(location.router)
app.include_router(lock.router)
app.include_router(log.router)
app.include_router(rental.router)
app.include_router(safe.router)
app.include_router(user.router)

use_route_names_as_operation_ids(app)
