from typing import Annotated

from annotated_types import Gt, Le
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
async def get_users(
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    return await storage.get_users()


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreate,
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    user: User = await storage.create_user(user_in=user_in)
    return user


@router.post(
    "/create-many",
    response_model=list[UserOut],
    status_code=status.HTTP_201_CREATED,
)
async def create_many_users(
    n_users: Annotated[int, Gt(0), Le(1000)],
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    users: list[User] = await storage.create_many_users(n_users=n_users)
    return users


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
async def delete_user(
    user: Annotated[User, Depends(get_user_by_id)],
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
) -> None:
    await storage.delete_user(user)


@router.patch("/{user_id}", response_model=UserOut)
async def update_user(
    user: Annotated[User, Depends(get_user_by_id)],
    user_in: UserUpdate,
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
):
    return await storage.update_user(
        user=user,
        user_in=user_in,
    )
