from fastapi import Header, HTTPException, status

from models import User
from . import crud


def get_user_by_token(
    token: str = Header(..., alias="x-auth-token"),
) -> User:
    user = crud.get_user_by_token(token=token)
    if user is not None:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid token",
    )
