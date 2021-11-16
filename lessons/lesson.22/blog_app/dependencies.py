from fastapi import Header, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from starlette.status import HTTP_401_UNAUTHORIZED

from blog_app import crud
from blog_app.models import User
from blog_app.models.db_async import get_session


async def get_user_by_token(
    token: str = Header(..., description="User auth token"),
    session: AsyncSession = Depends(get_session),
) -> User:
    user = await crud.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={"message": "Invalid token!"},
    )
