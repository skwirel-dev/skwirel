from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class Portfolio(BaseModel):
    __tablename__ = "portfolios"

    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    owner_id = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=False)

    owner = relationship("User", back_populates="portfolios")
    accounts = relationship("Account", back_populates="portfolio")
