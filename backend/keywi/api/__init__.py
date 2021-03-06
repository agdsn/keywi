from urllib.parse import urljoin

from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db
from starlette.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware

import model, model.base
from api import user, safe, rental, log, lock, location, key, auth
from api.helpers import use_route_names_as_operation_ids, SpaStaticFiles

from lib.app_config import app_config
from model.helper import init_data
from model.session import session

root_app = FastAPI(root_path=app_config.get('general', 'root_path', fallback=''))

app = FastAPI(title="Keywi", version="0.0.1", root_path=app_config.get('general', 'root_path', fallback=''))
app.add_middleware(DBSessionMiddleware, db_url=app_config.get('database', 'url'))

# add cors specification
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8080", "https://keywi.agdsn.de"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

app.add_middleware(SessionMiddleware, secret_key=app_config.get('general', 'session_secret'))

with db():
    model.base.ModelBase.metadata.create_all(session.get_bind())

    if len(session.query(model.User).all()) == 0:
        init_data(_commit=True)

app.include_router(key.router)
app.include_router(location.router)
app.include_router(lock.router)
app.include_router(log.router)
app.include_router(rental.router)
app.include_router(safe.router)
app.include_router(user.router)
app.include_router(auth.router)

use_route_names_as_operation_ids(app)

root_app.mount('/api', app)
root_app.mount('/', SpaStaticFiles(directory="web", html=True), name="web")
