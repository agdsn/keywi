from typing import List

from fastapi import APIRouter, Security
from fastapi_sqlalchemy import db

from api.auth import CurrentUser
from model import LogEntry
from model.pydantic import  LogEntryModel

router = APIRouter(prefix="/log", tags=["log"])


@router.get("/", response_model=List[LogEntryModel],
            dependencies=[Security(CurrentUser(), scopes=['log:read', 'log:self:read'])])
def get_logs():
    return db.session.query(LogEntry).all()
