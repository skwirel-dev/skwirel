from sqlalchemy import Column, Enum, ForeignKey, Numeric, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class CostBasisMethod(str):
    FIFO = "fifo"
    WEIGHTED_AVERAGE = "weighted_average"


class TaxLot(BaseModel):
    __tablename__ = "tax_lots"

    position_id = Column(UUID(as_uuid=True), ForeignKey("positions.id"), nullable=False)
    transaction_id = Column(
        UUID(as_uuid=True), ForeignKey("transactions.id"), nullable=False
    )
    shares = Column(Numeric(18, 8), nullable=False)
    cost_per_share = Column(Numeric(18, 4), nullable=False)
    acquired_date = Column(String, nullable=False)
    method = Column(String, default=CostBasisMethod.FIFO.value)

    position = relationship("Position", back_populates="tax_lots")
    transaction = relationship("Transaction", back_populates="tax_lots")
