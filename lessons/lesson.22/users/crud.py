"""
C - create
R - read
U - update
D - delete
"""
from time import time
from typing import Optional

import requests
from sqlalchemy.orm import Session

from models import User
from .schemas import UserIn


def list_users(session: Session) -> list[User]:
    return session.query(User).order_by(User.id).all()


def create_user(session: Session, user_in: UserIn) -> User:
    user = User(**user_in.dict())
    print("created user", user)

    session.add(user)
    session.commit()

    return user


def create_many_users(session: Session, count: int) -> list[User]:
    current_time = int(time()) % 1000
    users = [
        User(username=f"user_{current_time}_{i:03d}")
        for i in range(1, count + 1)
    ]
    session.add_all(users)
    session.commit()
    return users


def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    try:
        resp = requests.get("https://httpbin.org/get")
        resp.json()
    except:
        pass

    user = session.get(User, user_id)
    return user


def get_user_by_token(session: Session, token: str) -> Optional[User]:
    user = session.query(User).filter(User.token == token).one_or_none()
    return user
