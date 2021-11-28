from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from starlette.middleware.cors import CORSMiddleware

import model, model.base
from api import user, safe, rental, log, lock, location, key
from api.helpers import use_route_names_as_operation_ids

from lib.app_config import app_config


app = FastAPI(title="Keywi", version="0.0.1",
              servers=[{"url": 'http://localhost:6080', "description": "main"}])
app.add_middleware(DBSessionMiddleware, db_url=app_config.get('database', 'url'))

# add cors specification
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

with db():
    model.base.ModelBase.metadata.create_all(db.session.get_bind())

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(key.router)
app.include_router(location.router)
app.include_router(lock.router)
app.include_router(log.router)
app.include_router(rental.router)
app.include_router(safe.router)
app.include_router(user.router)

use_route_names_as_operation_ids(app)
