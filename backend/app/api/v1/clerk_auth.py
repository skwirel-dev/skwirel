"""Clerk authentication integration with optional dev mode."""

from typing import Optional
from uuid import UUID

from fastapi import Depends, HTTPException, Request, status
from jose import JWTError, jwt
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.database import get_db
from app.models.user import User
from app.schemas.user import PrincipalSchema


def _serialize_principal(user: User) -> PrincipalSchema:
    """Serialize a User model into a PrincipalSchema with license_key."""
    return PrincipalSchema(
        id=user.id,
        email=user.email,
        full_name=user.full_name,
        license_key=user.license_key,
        clerk_user_id=user.clerk_user_id,
    )


async def get_optional_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> Optional[PrincipalSchema]:
    """
    Optional auth dependency - returns None if no valid auth.
    Use this for routes that work both authenticated and anonymous.
    """
    if settings.DEV_AUTH_MODE:
        dev_user = await _get_dev_user(db)
        if dev_user:
            return _serialize_principal(dev_user)
        return None

    authorization = request.headers.get("Authorization")
    if not authorization or not authorization.startswith("Bearer "):
        return None

    token = authorization.replace("Bearer ", "")
    try:
        payload = jwt.decode(
            token,
            settings.CLERK_SECRET_KEY,
            algorithms=[settings.CLERK_JWT_ALGORITHM],
        )
        clerk_user_id = payload.get("sub")
        if not clerk_user_id:
            return None
    except JWTError:
        return None

    result = await db.execute(select(User).where(User.clerk_user_id == clerk_user_id))
    user = result.scalar_one_or_none()
    if not user or not user.is_active:
        return None

    return _serialize_principal(user)


async def get_current_user(
    request: Request,
    db: AsyncSession = Depends(get_db),
) -> PrincipalSchema:
    """
    Required auth dependency - raises 401 if no valid auth.
    Use this for protected routes.
    """
    user = await get_optional_user(request, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


async def _get_dev_user(db: AsyncSession) -> Optional[User]:
    """Get or create dev user for local development."""
    result = await db.execute(select(User).where(User.id == UUID(settings.DEV_USER_ID)))
    user = result.scalar_one_or_none()

    if not user:
        user = User(
            id=UUID(settings.DEV_USER_ID),
            email="dev@localhost",
            hashed_password="dev-mode-no-password",
            full_name="Development User",
            is_active=True,
            license_key="DEV_LICENSE_KEY",
        )
        db.add(user)
        await db.flush()

    return user
