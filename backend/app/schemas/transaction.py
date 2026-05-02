from datetime import datetime
from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class TransactionBase(BaseModel):
    symbol: str
    transaction_type: str
    shares: Decimal
    price: Decimal
    total_amount: Decimal
    fees: Optional[Decimal] = None
    settlement_date: Optional[str] = None
    notes: Optional[str] = None


class TransactionCreate(TransactionBase):
    account_id: UUID


class TransactionUpdate(BaseModel):
    symbol: Optional[str] = None
    transaction_type: Optional[str] = None
    shares: Optional[Decimal] = None
    price: Optional[Decimal] = None
    total_amount: Optional[Decimal] = None
    fees: Optional[Decimal] = None
    settlement_date: Optional[str] = None
    notes: Optional[str] = None


class TransactionResponse(TransactionBase):
    id: UUID
    account_id: UUID
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
