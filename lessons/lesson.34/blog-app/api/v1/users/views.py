from fastapi import APIRouter

from api.v1.users.dependencies import GetCrud, GetUser
from models import User
from schemas.user import UserRead

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get(
    "/",
    response_model=list[UserRead],
)
def get_users(
    crud: GetCrud,
) -> list[User]:
    return crud.get_users()


@router.get(
    "/{user_id}/",
    response_model=UserRead,
)
def get_user(
    user: GetUser,
) -> User:
    return user
