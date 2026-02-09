from fastapi import APIRouter, status

from models import User
from schemas import UserCreate, UserRead

from .dependencies import GetCRUD, GetUserByID


router = APIRouter(
    tags=["Users"],
    prefix="/users",
)


@router.get(
    "/",
    response_model=list[UserRead],
)
async def get_users(
    crud: GetCRUD,
) -> list[User]:
    return await crud.get_users()


@router.post(
    "/",
    response_model=UserRead,
    status_code=status.HTTP_201_CREATED,
)
async def create_user(
    user_create: UserCreate,
    crud: GetCRUD,
) -> User:
    return await crud.create_user(
        user_create=user_create,
    )


@router.get(
    "/{user_id}/",
    response_model=UserRead,
)
def get_user_by_id(
    user: GetUserByID,
) -> User:
    return user
