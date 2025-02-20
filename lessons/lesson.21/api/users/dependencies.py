from typing import Annotated

from fastapi import Header, HTTPException, status

from . import schemas
from .crud import users


def get_user_by_token(
    token: Annotated[str, Header(alias="x-auth-token")],
) -> schemas.User:
    user = users.get_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )
