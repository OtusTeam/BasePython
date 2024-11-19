from collections.abc import Generator

from fastapi import Depends, HTTPException, status
from pydantic import EmailStr
from sqlalchemy.orm import Session

from models import Author
from models.db import session_factory
from .crud import AuthorStorage


def session_dependency() -> Generator[Session]:
    with session_factory() as session:
        yield session


def authors_crud_dependency(
    session: Session = Depends(session_dependency),
) -> AuthorStorage:
    return AuthorStorage(session=session)


def get_author_by_email(
    # email: EmailStr = Header(),
    # email: EmailStr = Path(),
    email: EmailStr,
    storage: AuthorStorage = Depends(authors_crud_dependency),
) -> Author:
    author = storage.get_by_email(email=email)
    if author:
        return author

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Author by email not found",
    )
