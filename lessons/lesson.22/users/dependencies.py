
from fastapi import Header, HTTPException, status, Depends
from sqlalchemy.orm import Session

from models import User
from models.db_sync import get_session
from . import crud


def get_user_by_token(
    session: Session = Depends(get_session),
    token: str = Header(
        ...,
        description="User Auth Token",
        alias="x-auth-token",
    ),
) -> User:

    user = crud.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid auth token",
    )

