import logging
from time import time, sleep
from typing import Optional

import requests
from sqlalchemy.orm import Session
from sqlalchemy.exc import DatabaseError

from fastapi.exceptions import HTTPException
from fastapi import status

from models import User
from .schemas import UserIn as UserInSchema

log = logging.getLogger(__name__)


def list_users(session: Session) -> list[User]:
    return session.query(User).all()


def create_user(session: Session, user_in: UserInSchema) -> User:
    user = User(**user_in.dict())

    session.add(user)
    try:
        session.commit()
    except DatabaseError as e:
        log.exception("could not save user")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e),
        )

    session.refresh(user)
    return user


def create_many_users(session: Session, count: int) -> list[User]:
    current_time = int(time()) % 10000
    users = [
        User(username=f"user_{current_time}_{i:03d}")
        for i in range(1, count + 1)
    ]
    session.add_all(users)
    session.commit()
    return users


def get_user(session: Session, user_id: int) -> Optional[User]:
    try:
        response = requests.get("https://httpbin.org/get")
        response.json()
    except:
        pass

    return session.get(User, user_id)


def get_user_by_token(session: Session, token: str) -> Optional[User]:
    user = (
        session
        .query(User)
        .filter(User.token == token)
        .one_or_none()
    )
    return user
