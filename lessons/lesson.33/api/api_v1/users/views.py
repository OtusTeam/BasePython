from fastapi import APIRouter, status

from api.api_v1.users.dependencies import GetUsersCRUD, GetUserById
from models import User
from schemas.user import UserReadSchema, UserCreateSchema

router = APIRouter(
    prefix="/users",
)


@router.get(
    "/",
    response_model=list[UserReadSchema],
)
def get_users(
    crud: GetUsersCRUD,
) -> list[User]:
    return crud.get_list()


@router.post(
    "/",
    response_model=UserReadSchema,
)
def create_user(
    user_in: UserCreateSchema,
    crud: GetUsersCRUD,
) -> User:
    return crud.create(user_in)


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
