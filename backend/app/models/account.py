from sqlalchemy import Column, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class Account(BaseModel):
    __tablename__ = "accounts"

    name = Column(String, nullable=False)
    account_type = Column(String, nullable=False)
    institution = Column(String, nullable=True)
    account_number_masked = Column(String, nullable=True)
    portfolio_id = Column(
        UUID(as_uuid=True), ForeignKey("portfolios.id"), nullable=False
    )

    portfolio = relationship("Portfolio", back_populates="accounts")
    positions = relationship("Position", back_populates="account")
    transactions = relationship("Transaction", back_populates="account")
