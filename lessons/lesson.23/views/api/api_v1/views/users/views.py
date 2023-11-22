from fastapi import APIRouter, HTTPException, status

from models import User
from views.api.schemas import UserSchema, UserCreateSchema
from . import crud

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/", response_model=list[UserSchema])
def get_users() -> list[User]:
    return crud.get_users()


@router.get("/{user_id}/", response_model=UserSchema)
def get_user_by_id(user_id: int) -> User:
    user: User | None = crud.get_user_by_id(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="user_not_found",
    )


@router.post("/", response_model=UserSchema)
def create_user(
    user_create: UserCreateSchema,
):
    return crud.create_user(user_create=user_create)
