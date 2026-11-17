"""Request parameters and checks shared by the handlers."""

import logging
from collections.abc import Iterator
from typing import Annotated

from fastapi import HTTPException, status, Query, Depends, Header, Request
from pydantic import BaseModel

from app.catalog import USERS, User, BookService, AuthorService

logger = logging.getLogger(__name__)



class Pagination(BaseModel):
    offset: Annotated[int, Query(ge=0)] = 0
    limit: Annotated[int, Query(ge=1, le=20)] = 3


type Page = Annotated[Pagination, Query()]


def get_current_user(
    x_user: Annotated[str | None, Header()] = None,
) -> User:
    logger.info("get_current_user: looking up %s", x_user)
    if x_user is None or x_user not in USERS:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Use X-User: alice (active) or X-User: bob (inactive)",
        )
    return USERS[x_user]


type CurrentUser = Annotated[User, Depends(get_current_user)]


def require_active_user(user: User) -> None:
    """Stop the request before the handler if the reader is inactive.

    Raises:
        HTTPException: If the reader is inactive.

    """
    if not user.active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Reader is inactive",
        )


def get_current_active_user(
    user: CurrentUser,
) -> User:
    require_active_user(user)
    return user


type CurrentActiveUser = Annotated[User, Depends(get_current_active_user)]


def get_book_service() -> BookService:
    return BookService()


type Books = Annotated[BookService, Depends(get_book_service)]


def get_author_service() -> AuthorService:
    # with session() as sess:
    #     try:
    #         yield AuthorService(sess)
    #     except Exception:
    #         sess.rollback()
    return AuthorService()


type Authors = Annotated[AuthorService, Depends(get_author_service)]


def trace_scope(
    request: Request,
) -> Iterator[None]:
    logger.info("[%s] dependency trace ENTER", request.url.path)
    try:
        yield
    finally:
        logger.info("[%s] dependency trace EXIT", request.url.path)
