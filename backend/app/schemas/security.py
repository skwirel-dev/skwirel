from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SecurityBase(BaseModel):
    symbol: str
    name: str
    asset_class: str | None = None
    exchange: str | None = None


class SecurityCreate(SecurityBase):
    pass


class SecurityUpdate(BaseModel):
    symbol: str | None = None
    name: str | None = None
    asset_class: str | None = None
    exchange: str | None = None


class SecurityResponse(SecurityBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
