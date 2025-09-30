from typing import Annotated

from fastapi import APIRouter
from fastapi.params import Depends
from starlette import status

from api.api_v2.users.dependencies import GetUsersCRUD, get_user_by_id
from models import User
from schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/",
    response_model=list[UserReadSchema],
)
async def get_users_list(
    crud: GetUsersCRUD,
) -> list[User]:
    return await crud.get_list()


@router.get(
    "/{user_id}/",
    response_model=UserReadSchema,
)
def get_user(
    user: Annotated[
        User,
        Depends(get_user_by_id),
    ],
) -> User:
    return user


@router.post(
    "/",
    response_model=UserReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_create: UserCreateSchema,
    crud: GetUsersCRUD,
) -> User:
    return await crud.create(user_create)


@router.post(
    "/create-many",
    response_model=list[UserReadSchema],
    status_code=status.HTTP_201_CREATED,
)
async def create_many_users(
    n_users: int,
    crud: GetUsersCRUD,
) -> list[User]:
    return await crud.create_many(n_users)
