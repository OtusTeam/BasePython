"""
Create
Read
Update
Delete
"""
from models import User
from models.db_sync import Session

from .schemas import UserIn


def get_users() -> list[User]:
    return Session.query(User).order_by(User.id).all()


def create_user(user_in: UserIn) -> User:
    user = User(**user_in.model_dump())
    Session.add(user)
    Session.commit()
    return user


def get_user_by_id(user_id: int) -> User | None:
    return Session.get(User, user_id)


def get_user_by_token(token: str) -> User | None:
    return Session.query(User).filter(User.token == token).one_or_none()
