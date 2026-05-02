from sqlalchemy import Column, String
from sqlalchemy.dialects.postgresql import UUID

from app.core.base import BaseModel


class Security(BaseModel):
    __tablename__ = "securities"

    symbol = Column(String, unique=True, nullable=False, index=True)
    name = Column(String, nullable=False)
    asset_class = Column(String, nullable=True)
    exchange = Column(String, nullable=True)
