from sqlalchemy import Column, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class Position(BaseModel):
    __tablename__ = "positions"

    account_id = Column(UUID(as_uuid=True), ForeignKey("accounts.id"), nullable=False)
    symbol = Column(String, nullable=False, index=True)
    shares = Column(Numeric(18, 8), nullable=False, default=0)
    cost_basis = Column(Numeric(18, 2), nullable=False, default=0)

    account = relationship("Account", back_populates="positions")
    tax_lots = relationship("TaxLot", back_populates="position")
