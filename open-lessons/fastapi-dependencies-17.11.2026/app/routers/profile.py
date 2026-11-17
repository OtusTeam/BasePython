from fastapi import APIRouter

from app.catalog import User
from app.dependencies import CurrentActiveUser, CurrentUser

router = APIRouter(tags=["profile"])


@router.get("/me")
def read_profile(
    user: CurrentUser,
    active_user: CurrentActiveUser,
) -> User:
    return user
