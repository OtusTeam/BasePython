from typing import Annotated

from fastapi import APIRouter, HTTPException, status, Depends

from pydantic import PositiveInt
from . import schemas
from .dependencies import get_user_by_token
from .crud import users

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "",
    response_model=list[schemas.UserRead],
)
def get_users():
    return users.get()


@router.post(
    "",
    response_model=schemas.UserRead,
)
def create_user(
    user_in: schemas.UserCreate,
):
    return users.create(user_in=user_in)


@router.get(
    "/me",
    response_model=schemas.UserRead,
)
def get_me(
    user: Annotated[schemas.User, Depends(get_user_by_token)],
):
    return user


@router.get(
    "/{user_id}",
    response_model=schemas.UserRead,
)
def get_user(user_id: PositiveInt) -> schemas.User:
    user = users.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
