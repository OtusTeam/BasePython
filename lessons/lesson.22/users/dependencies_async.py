
from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import get_session_async
from . import crud_async as crud


async def get_user_by_token(
    session: AsyncSession = Depends(get_session_async),
    token: str = Header(
        ...,
        description="User Auth Token",
        alias="x-auth-token",
    ),
) -> User:

    user = await crud.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid auth token",
    )

