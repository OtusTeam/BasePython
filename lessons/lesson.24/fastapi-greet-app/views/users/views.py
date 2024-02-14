from typing import Annotated

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    status,
)

from sqlalchemy.orm import Session

from models import User
from .dependencies import get_user_by_token, get_session
from . import crud
from .schemas import UserOut, UserCreate, UsersDataOut
from ..common.schemas import LimitOffsetPaginationSchema

router = APIRouter()


@router.get("/", response_model=UsersDataOut)
def get_users(
    pagination: LimitOffsetPaginationSchema = Depends(LimitOffsetPaginationSchema),
    session: Session = Depends(get_session),
):
    users: list[User] = crud.get_users(
        session=session,
        limit=pagination.limit,
        offset=pagination.offset,
    )
    users_count = crud.get_users_count(session)
    return UsersDataOut(
        data=users,
        meta={
            "pagination": {
                "total_count": users_count,
                **pagination.model_dump(),
            },
        },
    )


@router.get("/all/", response_model=list[UserOut])
def get_users(
    session: Session = Depends(get_session),
):
    return crud.get_users(session=session)


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
def create_user(
    user_in: UserCreate,
    session: Session = Depends(get_session),
):
    return crud.create_user(session=session, user_in=user_in)


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
def get_user(
    user_id: int,
    session: Session = Depends(get_session),
):
    user: User | None = crud.get_user(
        session=session,
        user_id=user_id,
    )
    if user:
        return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found",
    )
