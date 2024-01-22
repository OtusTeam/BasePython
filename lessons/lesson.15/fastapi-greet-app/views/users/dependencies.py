from typing import Annotated

from fastapi import Header, HTTPException
from starlette import status

from .crud import storage
from .schemas import User


def get_user_by_token(
    token: Annotated[
        str,
        Header(alias="x-auth-token"),
    ],
) -> User:
    user: User | None = storage.get_user_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
    )
