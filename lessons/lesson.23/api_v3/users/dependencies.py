from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import scoped_session_dependency
from . import crud


async def get_user_by_token(
    token: str = Header(..., alias="x-auth-token"),
    session: AsyncSession = Depends(scoped_session_dependency),
) -> User:
    user: User = await crud.get_user_by_token(session=session, token=token)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )
