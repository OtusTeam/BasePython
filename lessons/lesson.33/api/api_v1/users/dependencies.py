from typing import Annotated
from collections.abc import Generator

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import PositiveInt

from api.api_v1.users.crud import UsersCRUD
from models import session_factory, User


def get_session() -> Generator[Session]:
    with session_factory() as session:
        yield session


GetSession = Annotated[
    Session,
    Depends(get_session),
]


def get_users_crud(
    session: GetSession,
) -> UsersCRUD:
    return UsersCRUD(session)


GetUsersCRUD = Annotated[
    UsersCRUD,
    Depends(get_users_crud),
]


def get_user_by_id(
    user_id: Annotated[
        PositiveInt,
        Path(),
    ],
    crud: GetUsersCRUD,
) -> User:
    user: User | None = crud.get_by_id(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
