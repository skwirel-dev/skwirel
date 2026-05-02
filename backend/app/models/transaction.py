from sqlalchemy import Column, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class TransactionType(str):
    BUY = "buy"
    SELL = "sell"
    DIVIDEND = "dividend"
    SPLIT = "split"


class Transaction(BaseModel):
    __tablename__ = "transactions"

    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    symbol = Column(String, nullable=False, index=True)
    transaction_type = Column(String, nullable=False)
    shares = Column(Numeric(18, 8), nullable=False)
    price = Column(Numeric(18, 4), nullable=False)
    total_amount = Column(Numeric(18, 2), nullable=False)
    fees = Column(Numeric(18, 2), nullable=True)
    settlement_date = Column(String, nullable=True)
    notes = Column(String, nullable=True)

    account = relationship("Account", back_populates="transactions")
    tax_lots = relationship("TaxLot", back_populates="transaction")
