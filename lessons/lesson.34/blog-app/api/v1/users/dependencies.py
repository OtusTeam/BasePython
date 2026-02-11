from typing import Annotated

from fastapi import Depends, Path, status, HTTPException

from api.dependencies.session import GetSession
from models import User
from .crud import Crud


def get_crud(
    session: GetSession,
) -> Crud:
    return Crud(session)


GetCRUD = Annotated[
    Crud,
    Depends(get_crud),
]


def get_user_by_id(
    user_id: Annotated[
        int,
        Path(),
    ],
    crud: GetCRUD,
) -> User:
    user = crud.get_user(user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )


GetUserByID = Annotated[
    User,
    Depends(get_user_by_id),
]
