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

from .crud import storage
from .schemas import User

http_bearer = HTTPBearer(auto_error=True)


def get_user_by_auth_token(
    # token: Annotated[str, Header(alias="auth-token")],
    token: Annotated[HTTPAuthorizationCredentials, Depends(http_bearer)],
) -> User:
    user = storage.get_by_token(token=token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail="Invalid token",
    )
