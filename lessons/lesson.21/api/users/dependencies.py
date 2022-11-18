from fastapi import HTTPException, status, Header, Depends
from sqlalchemy.orm import Session

from models.dependency_sync import get_session
from . import crud
from models import User


def get_user_by_token(
    token: str = Header(alias="x-auth-token"),
    session: Session = Depends(get_session),
) -> User:
    user = crud.get_user_by_token(session, token)
    if user:
        return user

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
    )
