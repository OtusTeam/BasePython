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
from sqlalchemy.ext.asyncio import AsyncSession

from models import User
from models.db_async import get_async_session

from .crud import UsersStorage

http_bearer = HTTPBearer(auto_error=True)


def get_users_storage(
    session: Annotated[
        AsyncSession,
        Depends(get_async_session),
    ]
) -> UsersStorage:
    return UsersStorage(session=session)


async def get_user_by_auth_token(
    storage: Annotated[
        UsersStorage,
        Depends(get_users_storage),
    ],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> User:
    user: User | None = await storage.get_by_token(token=token.credentials)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )
