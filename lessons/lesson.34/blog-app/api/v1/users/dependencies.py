from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, Path, HTTPException, status
from pydantic import PositiveInt
from sqlalchemy.orm import Session

from api.v1.users.crud import Crud
from models import User
from models.db import session_factory


def get_session() -> Generator[Session]:
    with session_factory() as session:
        try:
            yield session
        except Exception:
            session.rollback()
            raise


GetSession = Annotated[
    Session,
    Depends(get_session),
]


def get_crud(
    session: GetSession,
) -> Crud:
    return Crud(session)


GetCrud = Annotated[
    Crud,
    Depends(get_crud),
]


def get_user(
    user_id: Annotated[PositiveInt, Path()],
    crud: GetCrud,
) -> User:
    user = crud.get_user(user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )


GetUser = Annotated[
    User,
    Depends(get_user),
]
