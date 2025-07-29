from typing import Annotated

from fastapi import APIRouter, Depends

from api.api_v1.users.crud import UsersCRUD
from api.api_v1.users.dependencies import users_crud, get_user_by_id
from models import User
from schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(
    prefix="/users",
    tags=["User"],
)


@router.get("/", response_model=list[UserReadSchema])
def get_users(
    crud: Annotated[
        UsersCRUD,
        Depends(users_crud),
    ],
) -> list[User]:
    return crud.get_list()


@router.get("/{user_id}/", response_model=UserReadSchema)
def get_user(
    user: Annotated[
        User,
        Depends(get_user_by_id),
    ],
) -> User:
    return user


@router.post("/", response_model=UserReadSchema)
def create_user(
    user_create: UserCreateSchema,
    crud: Annotated[
        UsersCRUD,
        Depends(users_crud),
    ],
) -> User:
    return crud.create(user_create)
