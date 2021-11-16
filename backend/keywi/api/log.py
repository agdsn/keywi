from typing import List

from fastapi import APIRouter
from fastapi_sqlalchemy import db

from model import LogEntry
from model.pydantic import  LogEntryModel

router = APIRouter(prefix="/logs", tags=["logs"])


@router.get("/", response_model=List[LogEntryModel])
def get_logs():
    return db.session.query(LogEntry).all()
