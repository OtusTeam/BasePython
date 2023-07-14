from fastapi import APIRouter, HTTPException, status, Depends

from . import crud
from .dependencies import get_user_by_token
from .schemas import UserIn, UserOut, User

router = APIRouter(tags=["Users"])


@router.get("/", response_model=list[UserOut])
def get_users() -> list[UserOut]:
    return crud.get_users()


@router.post(
    "/",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
    responses={
        status.HTTP_201_CREATED: {
            "model": UserOut,
        }
    }
)
def create_user(user_in: UserIn):
    return crud.create_user(user_in=user_in)


@router.get("/me/", response_model=UserOut)
def get_me(user: User = Depends(get_user_by_token)):
    return user


@router.get(
    "/{user_id}/",
    response_model=UserOut,
    responses={
        status.HTTP_404_NOT_FOUND: {"description": "Not found"},
    },
)
def get_user_by_id(user_id: int):
    user = crud.get_user_by_id(user_id=user_id)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User #{user_id} not found!"
    )
