from fastapi import (
    APIRouter,
    HTTPException,
    status,
    Depends,
)
from pydantic import PositiveInt

from views.users.schemas import (
    UserRead,
    UserCreate,
    User,
)

from .crud import storage
from .dependencies import get_user_by_auth_token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get(
    "/",
    response_model=list[UserRead],
)
def get_users_list():
    return storage.get()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserRead,
)
def create_user(
    user_in: UserCreate,
):
    return storage.create(user_in=user_in)


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
def get_user(user_id: PositiveInt):
    user = storage.get_by_id(user_id=user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
