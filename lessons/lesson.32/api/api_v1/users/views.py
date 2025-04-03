from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from pydantic import PositiveInt

from schemas import UserRead, UserCreate
from models import User
from .crud import UsersCRUD
from .dependencies import get_user_by_token, users_crud


router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[UserRead],
)
def get_users(
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> list[User]:
    return crud.get()


@router.post(
    "",
    response_model=UserRead,
)
def create_user(
    user_in: UserCreate,
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> User:
    return crud.create(user_in=user_in)


@router.get(
    "/me",
    response_model=UserRead,
)
def get_me(
    user: Annotated[User, Depends(get_user_by_token)],
):
    return user


@router.get(
    "/{user_id}",
    response_model=UserRead,
)
def get_user(
    user_id: PositiveInt,
    crud: Annotated[UsersCRUD, Depends(users_crud)],
) -> User:
    user = crud.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
