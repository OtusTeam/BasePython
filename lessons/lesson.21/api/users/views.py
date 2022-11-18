from fastapi import APIRouter, HTTPException, Depends
from starlette import status
from sqlalchemy.orm import Session

from models import User
from models.dependency_sync import get_session
from api.schemas.user import UserOut, UserIn
from . import crud
from .dependencies import get_user_by_token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.get("", response_model=list[UserOut])
def list_users(
    session: Session = Depends(get_session),
) -> list[User]:
    return crud.get_users(session)


@router.post(
    "",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserIn,
    session: Session = Depends(get_session),
) -> User:
    return crud.create_user(session, user_in)


@router.get("/me", response_model=UserOut)
def get_me(
    user: User = Depends(get_user_by_token),
) -> User:
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    session: Session = Depends(get_session),
) -> User:
    user = crud.get_user_by_id(session, user_id)
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
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    crud.delete_user(session, user_id)
