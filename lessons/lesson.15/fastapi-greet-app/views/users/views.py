from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from .dependencies import get_user_by_token
from .crud import storage
from .schemas import UserOut, UserCreate, User

router = APIRouter()


@router.get("/", response_model=list[UserOut])
def get_users():
    return storage.get_users()


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_in: UserCreate):
    return storage.create_user(user_in=user_in)


@router.get(
    "/me/",
    response_model=UserOut,
    responses={
        status.HTTP_401_UNAUTHORIZED: {
            "description": "Not Authorized",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "Could not validate credentials",
                    },
                },
            },
        },
    },
)
def get_user_me(
    # user: User = Depends(get_user_by_token),
    user: Annotated[User, Depends(get_user_by_token)],
):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {
            "description": "User not found",
            "content": {
                "application/json": {
                    "example": {
                        "detail": "User #0 not found!",
                    },
                },
            },
        },
    },
)
def get_user(user_id: int):
    user: User | None = storage.get_user(user_id=user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
