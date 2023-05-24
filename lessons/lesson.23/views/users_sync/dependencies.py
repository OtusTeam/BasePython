from fastapi import HTTPException, status, Header, Depends
from sqlalchemy.orm import Session

from models import User
from models.db_sync import get_session
from . import crud


def get_user_by_auth_token(
    token: str = Header(..., alias="x-auth-token"),
    session: Session = Depends(get_session),
) -> User:
    user: User | None = crud.get_user_by_token(session=session, token=token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Auth token invalid!",
    )
