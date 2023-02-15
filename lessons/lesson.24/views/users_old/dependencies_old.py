from fastapi import Header, HTTPException, status, Depends

from models import User
from models.db_sync import Session
from .crud_old import get_user_by_token


def session_dependency():
    with Session() as session:
        yield session


def user_by_token(
    x_auth_token: str = Header(),
    session: Session = Depends(session_dependency),
) -> User:
    user = get_user_by_token(session, x_auth_token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth Token invalid!",
    )
