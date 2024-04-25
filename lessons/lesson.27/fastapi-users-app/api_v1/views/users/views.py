from typing import Annotated

from fastapi import (
    APIRouter,
    status,
    Depends,
)

from models import User
from schemas.user import (
    UserOut,
    UserCreate,
    UserUpdate,
)
from .crud import UsersStorage
from .dependencies.users_storage import get_users_storage
from .dependencies.user import (
    get_user_by_token,
    get_user_by_id,
)

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
def get_users(
    # storage: UsersStorage = Depends(get_users_storage),
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    return storage.get_users()


@router.post("", response_model=UserOut)
def create_user(
    user_in: UserCreate,
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    user: User = storage.create_user(user_in=user_in)
    return user


@router.get("/me", response_model=UserOut)
def get_current_user(
    user: Annotated[User, Depends(get_user_by_token)]
):
    return user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User with id #0 does not exist",
                    },
                },
            },
        },
    },
)
def get_user_by_id(
    user: Annotated[User, Depends(get_user_by_id)],
):
    return user


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(
    user: Annotated[User, Depends(get_user_by_id)],
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
) -> None:
    storage.delete_user(user)


@router.patch("/{user_id}", response_model=UserOut)
def update_user(
    user: Annotated[User, Depends(get_user_by_id)],
    user_in: UserUpdate,
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    return storage.update_user(
        user=user,
        user_in=user_in,
    )
