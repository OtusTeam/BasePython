from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pydantic import PositiveInt
from sqlalchemy.exc import IntegrityError, DatabaseError

from models import User
from schemas.user import (
    UserRead,
    UserCreate,
)

from .crud import UsersStorage
from .dependencies import get_user_by_auth_token, get_users_storage

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserRead],
)
def get_users_list(
    storage: Annotated[
        UsersStorage,
        Depends(get_users_storage),
    ],
):
    return storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead,
)
def create_user(
    storage: Annotated[
        UsersStorage,
        Depends(get_users_storage),
    ],
    user_in: UserCreate,
):
    try:
        return storage.create(
            user_in=user_in,
        )
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="User already exists (probably)",
        )
    except DatabaseError:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Database error",
        )


@router.get("/me/", response_model=UserRead)
def get_me(
    user: User = Depends(get_user_by_auth_token),
):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserRead,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User #0 not found",
                    },
                },
            },
        },
    },
)
def get_user(
    storage: Annotated[
        UsersStorage,
        Depends(get_users_storage),
    ],
    user_id: PositiveInt,
):
    user = storage.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
