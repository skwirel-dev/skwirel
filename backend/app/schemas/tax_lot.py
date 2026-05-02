from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TaxLotBase(BaseModel):
    shares: Decimal
    cost_per_share: Decimal
    acquired_date: str
    method: str = "fifo"


class TaxLotCreate(TaxLotBase):
    position_id: UUID
    transaction_id: UUID


class TaxLotUpdate(BaseModel):
    shares: Optional[Decimal] = None
    cost_per_share: Optional[Decimal] = None
    acquired_date: Optional[str] = None
    method: Optional[str] = None


class TaxLotResponse(TaxLotBase):
    id: UUID
    position_id: UUID
    transaction_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
