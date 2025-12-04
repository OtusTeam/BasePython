from fastapi import APIRouter, status

from api.api_v2.users.dependencies import GetUsersCRUD, GetUserById
from models import User
from schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(
    prefix="/users",
)


@router.get(
    "/",
    response_model=list[UserReadSchema],
)
async def get_users(
    crud: GetUsersCRUD,
) -> list[User]:
    return await crud.get_list()


@router.post(
    "/",
    response_model=UserReadSchema,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_in: UserCreateSchema,
    crud: GetUsersCRUD,
) -> User:
    return await crud.create(user_in)


@router.get(
    "/{user_id}/",
    response_model=UserReadSchema,
    responses={
        status.HTTP_200_OK: {"model": UserReadSchema},
        status.HTTP_404_NOT_FOUND: {},
    },
)
def get_user_by_id(
    user: GetUserById,
) -> User:
    return user


@router.post(
    "/create-many/",
    response_model=list[UserReadSchema],
    status_code=status.HTTP_201_CREATED,
)
async def create_many(
    n_users: int,
    crud: GetUsersCRUD,
) -> list[User]:
    return await crud.create_many(n_users)
