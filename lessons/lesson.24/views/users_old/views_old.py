from time import sleep

from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.orm import Session

from models import User
from . import crud_old as crud
from .dependencies_old import user_by_token, session_dependency
from schemas.user import UserIn, UserOut

router = APIRouter(prefix="/users", tags=["Users (old)"])


@router.get("", response_model=list[UserOut])
def get_users(
    session: Session = Depends(session_dependency),
) -> list[User]:
    return crud.get_users(session)


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserIn,
    session: Session = Depends(session_dependency),
) -> User:
    return crud.create_user(session, user_in)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(user_by_token)) -> User:
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    session: Session = Depends(session_dependency),
) -> User:
    sleep(0.5)
    user = crud.get_user(session, user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!",
    )


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_user(
    user_id: int,
    session: Session = Depends(session_dependency),
) -> None:
    return crud.delete_user(session, user_id)
