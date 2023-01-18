from fastapi import APIRouter, status, HTTPException, Depends

from . import crud
from .dependencies import user_by_token
from .schemas import User, UserIn, UserOut

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut])
def get_users() -> list[User]:
    return crud.get_users()


@router.post("", response_model=UserOut)
def create_user(user_in: UserIn) -> User:
    return crud.create_user(user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(user_by_token)) -> User:
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(user_id: int) -> User:
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
