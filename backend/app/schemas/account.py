from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class AccountBase(BaseModel):
    name: str
    account_type: str
    institution: Optional[str] = None
    account_number_masked: Optional[str] = None


class AccountCreate(AccountBase):
    portfolio_id: UUID


class AccountUpdate(BaseModel):
    name: Optional[str] = None
    account_type: Optional[str] = None
    institution: Optional[str] = None
    account_number_masked: Optional[str] = None


class AccountResponse(AccountBase):
    id: UUID
    portfolio_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True


class AccountWithPositions(AccountResponse):
    positions: list["PositionResponse"] = []
