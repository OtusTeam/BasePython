from collections.abc import AsyncGenerator

from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from models import Author
from models.db_async import async_session
from .crud import AuthorStorage


async def async_session_dependency() -> AsyncGenerator[AsyncSession]:
    async with async_session() as session:
        yield session


def authors_crud_dependency(
    session: AsyncSession = Depends(async_session_dependency),
) -> AuthorStorage:
    return AuthorStorage(session=session)


async def get_author_by_email(
    email: EmailStr,
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> Author:
    author = await storage.get_by_email(email=email)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Author by email not found",
    )
