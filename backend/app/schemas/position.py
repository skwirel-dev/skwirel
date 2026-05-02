from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class PositionBase(BaseModel):
    symbol: str
    shares: Decimal = Decimal("0")
    cost_basis: Decimal = Decimal("0")


class PositionCreate(PositionBase):
    account_id: UUID


class PositionUpdate(BaseModel):
    symbol: Optional[str] = None
    shares: Optional[Decimal] = None
    cost_basis: Optional[Decimal] = None


class PositionResponse(PositionBase):
    id: UUID
    account_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
