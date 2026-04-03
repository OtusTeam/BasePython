from fastapi import APIRouter

from api.v2.users.dependencies import GetCrud, GetUser
from models import User
from schemas.user import UserRead, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.post(
    "/",
    response_model=UserRead,
)
async def create_user(
    user_create: UserCreate,
    crud: GetCrud,
) -> User:
    return await crud.create_user(user_create=user_create)


@router.get(
    "/",
    response_model=list[UserRead],
)
async def get_users(
    crud: GetCrud,
) -> list[User]:
    return await crud.get_users()


@router.get(
    "/{user_id}/",
    response_model=UserRead,
)
async def get_user(
    user: GetUser,
) -> User:
    return user
