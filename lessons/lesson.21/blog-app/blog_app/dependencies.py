from fastapi import Header, exceptions, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from blog_app import crud
from blog_app.schemas import User
from core.models.db import get_session


async def get_user_by_token(
    token: str = Header(..., description="User auth token"),
    db_session: AsyncSession = Depends(get_session),
) -> User:
    user = await crud.get_user_by_token(token, db_session)
    if user:
        return user

    raise exceptions.HTTPException(
        401,
        {"message": "Invalid token"}
    )
