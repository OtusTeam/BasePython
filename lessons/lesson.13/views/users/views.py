from fastapi import APIRouter, status, HTTPException

from . import crud
from .schemas import User, UserIn

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("")
def get_users() -> list[User]:
    return crud.get_users()


@router.post("")
def create_user(user_in: UserIn) -> User:
    return crud.create_user(user_in)


@router.get("/{user_id}")
def get_user(user_id: int) -> User | None:
    user = crud.get_user(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(user_id: int) -> None:
    return crud.delete_user(user_id)
