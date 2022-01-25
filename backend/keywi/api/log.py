from typing import List
from uuid import UUID

from fastapi import APIRouter, Security, Query
from fastapi_sqlalchemy import db

from api.auth import CurrentUser
from model import LogEntry
from model.pydantic import  LogEntryModel

router = APIRouter(prefix="/log", tags=["log"])


@router.get("/", response_model=List[LogEntryModel],
            dependencies=[Security(CurrentUser(), scopes=['log:read', 'log:self:read'])])
def get_logs(location_id: UUID = Query(None),
             key_id: UUID = Query(None),
             user_id: UUID = Query(None),
             lock_id: UUID = Query(None),
             safe_id: UUID = Query(None),
             rental_id: UUID = Query(None),):
    args = {k: v for k, v in locals().items() if v is not None}

    return db.session.query(LogEntry).filter_by(**args).all()
