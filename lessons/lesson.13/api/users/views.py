from fastapi import APIRouter, HTTPException, Depends
from starlette import status

from .schemas import UserOut, UserIn, User
from . import crud
from .dependencies import get_user_by_token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
def list_users() -> list[UserOut]:
    return crud.get_users()


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(user_in: UserIn) -> UserOut:
    return crud.create_user(user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)) -> User:
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int) -> UserOut:
    user = crud.get_user_by_id(user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} doesn't exist!",
    )


@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_user(user_id: int):
    crud.delete_user(user_id)
