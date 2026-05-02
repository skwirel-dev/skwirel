from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PortfolioBase(BaseModel):
    name: str
    description: Optional[str] = None


class PortfolioCreate(PortfolioBase):
    pass


class PortfolioUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None


class PortfolioResponse(PortfolioBase):
    id: UUID
    owner_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class PortfolioWithAccounts(PortfolioResponse):
    accounts: list["AccountResponse"] = []
