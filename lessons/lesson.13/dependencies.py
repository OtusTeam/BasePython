from fastapi import Header, HTTPException

from starlette.status import HTTP_401_UNAUTHORIZED

import crud
from schemas import User


def get_user_by_token(token: str = Header(..., description="User auth token")) -> User:
    user = crud.get_user_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail={"message": "Invalid token!"},
    )
