from typing import Annotated

from fastapi import Depends, Path, HTTPException, status

from api.dependencies.session import GetSession
from api.v1.users.crud import Crud
from models import User


def get_crud(
    session: GetSession,
) -> Crud:
    return Crud(session)


GetCrud = Annotated[
    Crud,
    Depends(get_crud),
]


def get_user(
    user_id: Annotated[int, Path()],
    crud: GetCrud,
) -> User:
    user = crud.get_user(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )


GetUser = Annotated[
    User,
    Depends(get_user),
]
