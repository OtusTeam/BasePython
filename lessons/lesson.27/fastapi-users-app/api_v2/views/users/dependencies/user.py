from typing import Annotated

from fastapi import Header, Depends, HTTPException, status, Path

from models import User

from api_v2.views.users.crud import UsersStorage
from api_v2.views.users.dependencies.users_storage import get_users_storage


async def get_user_by_id(
    user_id: Annotated[int, Path()],
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
) -> User:
    user: User | None = await storage.get_user(user_id)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"User with id #{user_id} does not exist",
    )


async def get_user_by_token(
    token: Annotated[
        str,
        Header(alias="x-auth-token"),
    ],
    storage: Annotated[UsersStorage, Depends(get_users_storage)],
) -> User:
    user: User | None = await storage.get_user_by_token(token=token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials, invalid token",
    )
