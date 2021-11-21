from typing import Optional
from pydantic import UUID4, BaseModel, EmailStr, Field, validator


class ZoomEventBase(BaseModel):
    event_ts: int
    event: str
    payload: dict


class ZoomEventCreate(ZoomEventBase):
    pass


class ZoomEventRead(ZoomEventBase):
    id: int
