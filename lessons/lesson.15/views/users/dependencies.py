from fastapi import Header, HTTPException, status

from .crud import get_user_by_token
from .schemas import User


def user_by_token(x_auth_token: str = Header()) -> User:
    user = get_user_by_token(x_auth_token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth Token invalid!",
    )
