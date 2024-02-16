# from typing import AsyncGenerator
from typing import Annotated

from fastapi import Header, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from models import User
from models.db import async_session
from . import crud


# async def get_session() -> AsyncGenerator[AsyncSession, None]:
async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
        # try:
        #     yield session
        # finally:
        #     # optional! cleanup
        #     session.rollback()


async def get_user_by_token(
    token: Annotated[
        str,
        Header(alias="x-auth-token"),
    ],
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
        detail="Could not validate credentials",
    )
