from fastapi import HTTPException, status, Header

from . import crud
from .schemas import User


def get_user_by_token(token: str = Header(alias="x-auth-token")) -> User:
    user = crud.get_user_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
