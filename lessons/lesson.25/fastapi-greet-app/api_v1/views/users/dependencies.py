from typing import Annotated

from fastapi import Header, HTTPException, Depends
from sqlalchemy.orm import Session
from starlette import status

from models import User
from models.db import session as session_maker
from . import crud


def get_session() -> Session:
    with session_maker() as session:
        yield session
        # try:
        #     yield sess
        # finally:
        #     # optional! cleanup
        #     sess.rollback()


def get_user_by_token(
    token: Annotated[
        str,
        Header(alias="x-auth-token"),
    ],
    session: Session = Depends(get_session),
) -> User:
    user: User | None = crud.get_user_by_token(
        session=session,
        token=token,
    )
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
