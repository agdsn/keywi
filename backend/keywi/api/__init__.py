from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware, db

from lib.app_config import app_config
from model import base
from model import _all

app = FastAPI()
app.add_middleware(DBSessionMiddleware, db_url=app_config.get('database', 'url'))

with db():
    base.ModelBase.metadata.create_all(db.session.get_bind())

@app.get("/")
async def root():
    return {"message": "Hello World"}
