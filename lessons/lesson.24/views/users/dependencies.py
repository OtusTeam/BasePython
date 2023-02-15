from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import async_session
from .crud import get_user_by_token


async def session_dependency():
    async with async_session() as session:
        yield session


async def user_by_token(
    session: AsyncSession = Depends(session_dependency),
    x_auth_token: str = Header(),
) -> User:
    user = await get_user_by_token(session, x_auth_token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth Token invalid!",
    )
