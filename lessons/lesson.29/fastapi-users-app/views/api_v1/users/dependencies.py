from typing import Annotated

from fastapi import (
    HTTPException,
    Depends,
    status,
)
from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials,
)
from sqlalchemy.orm import Session

from models import User
from models.db import get_session
from .crud import UsersStorage

http_bearer = HTTPBearer(auto_error=True)


def get_users_storage(
    session: Annotated[
        Session,
        Depends(get_session),
    ]
) -> UsersStorage:
    return UsersStorage(session=session)


def get_user_by_auth_token(
    storage: Annotated[
        UsersStorage,
        Depends(get_users_storage),
    ],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> User:
    user = storage.get_by_token(token=token.credentials)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )
