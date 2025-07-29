from typing import Annotated, Generator

from fastapi import Depends, Path, HTTPException, status
from pydantic import PositiveInt
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
    return UsersCRUD(session=session)


def get_user_by_id(
    user_id: Annotated[PositiveInt, Path],
    crud: Annotated[
        UsersCRUD,
        Depends(users_crud),
    ],
) -> User:
    user: User | None = crud.get_by_id(user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
