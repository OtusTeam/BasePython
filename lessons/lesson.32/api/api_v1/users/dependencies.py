from typing import Annotated, Generator

from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.orm import Session

from api.api_v1.users.crud import UsersCRUD
from models import User
from models.db import session_factory


def get_session() -> Generator[Session]:
    with session_factory() as session:
        yield session


def users_crud(
    session: Annotated[
        Session,
        Depends(get_session),
    ],
) -> UsersCRUD:
    return UsersCRUD(session)


def get_user_by_token(
    crud: Annotated[UsersCRUD, Depends(users_crud)],
    token: Annotated[str, Header(alias="x-auth-token")],
) -> User:
    user = crud.get_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )
