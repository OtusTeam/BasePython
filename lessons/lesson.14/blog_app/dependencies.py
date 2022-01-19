from fastapi import Header, HTTPException, status

from blog_app import crud
from blog_app.schemas import User


def get_user_by_auth_token(token: str = Header(..., description="User auth token")) -> User:
    user = crud.get_user_by_token(token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={"message": "Invalid token!"},
    )
