from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_404_NOT_FOUND
from sqlalchemy.orm import Session as SessionType

from models import User
from . import crud
from .dependencies import get_db_sync, get_user_by_auth_token
from .schemas import UserIn, UserOut

router = APIRouter(tags=["Users Sync"])


@router.get("", response_model=list[UserOut])
def list_users(
    session: SessionType = Depends(get_db_sync),
):
    return crud.list_users(session)


@router.post("", response_model=UserOut)
def create_user(
    user_in: UserIn,
    session: SessionType = Depends(get_db_sync),
):
    return crud.create_user(session, user_in)


@router.post("/many", response_model=list[UserOut])
def create_many_users(
    count: int = 500,
    session: SessionType = Depends(get_db_sync),
):
    return crud.create_many_users(session, count)


@router.get("/me", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_auth_token)):
    return user


@router.get(
    "/{user_id}",
    response_model=UserOut,
    responses={
        HTTP_404_NOT_FOUND: {
            "description": "user not found",
            "content": {
                "application/json": {
                    "schema": {
                        "title": "Not Found",
                        "type": "object",
                        "properties": {
                            "detail": {
                                "title": "Detail",
                                "type": "string",
                                "example": "user #0 not found",
                            },
                        },
                    },
                },
            },
        },
    },
)
def get_user_by_id(
    user_id: int,
    session: SessionType = Depends(get_db_sync),
):
    user = crud.get_user(session, user_id)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
