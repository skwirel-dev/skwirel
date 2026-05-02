from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from app.core.base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    full_name = Column(String, nullable=True)
    is_active = Column(Boolean, default=True, nullable=False)

    # Clerk integration
    clerk_user_id = Column(String, unique=True, nullable=True, index=True)

    # License context - attached to session on auth
    license_key = Column(String, nullable=True, index=True)

    portfolios = relationship("Portfolio", back_populates="owner")
