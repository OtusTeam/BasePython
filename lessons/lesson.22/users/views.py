
from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session

from models import User
from models.db_sync import get_session
from .schemas import UserIn, UserOut
from . import crud
from .dependencies import get_user_by_token

router = APIRouter(prefix="/sync/users", tags=["Users Sync"])


@router.get("", response_model=list[UserOut])
def list_users(
    session: Session = Depends(get_session),
):
    return crud.list_users(session)


@router.post("", response_model=UserOut)
def create_user(
    user_in: UserIn,
    session: Session = Depends(get_session),
):
    return crud.create_user(session, user_in=user_in)


@router.post("/many", response_model=list[UserOut])
def create_many_users(
    count: int,
    session: Session = Depends(get_session),
) -> list[User]:
    return crud.create_many_users(session, count)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@router.get("/{user_id}", response_model=UserOut)
def get_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user = crud.get_user_by_id(session, user_id)
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
