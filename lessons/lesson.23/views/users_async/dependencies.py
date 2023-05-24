from fastapi import HTTPException, status, Header, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import get_session
from . import crud


async def get_user_by_auth_token(
    token: str = Header(..., alias="x-auth-token"),
    session: AsyncSession = Depends(get_session),
) -> User:
    user: User | None = await crud.get_user_by_token(
        session=session,
        token=token,
    )
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth token invalid!",
    )
