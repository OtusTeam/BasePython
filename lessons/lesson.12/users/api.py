from fastapi import APIRouter, HTTPException, Depends
from starlette.status import HTTP_404_NOT_FOUND

from . import crud
from .dependencies import get_user_by_auth_token
from .schemas import UserIn, UserOut, User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=list[UserOut])
def list_users():
    return crud.list_users()


@router.post("", response_model=UserOut)
def create_user(user_in: UserIn):
    return crud.create_user(user_in)


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
def get_user_by_id(user_id: int):
    user = crud.get_user(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_404_NOT_FOUND,
        detail=f"user #{user_id} not found!",
    )
