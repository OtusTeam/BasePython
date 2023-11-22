from sqlalchemy import select

import requests

from models import User
from models.db_sync import Session
from views.api.schemas import UserCreateSchema


def get_users() -> list[User]:
    stmt = select(User).order_by(User.id)
    return list(Session.scalars(stmt).all())


def get_user_by_id(
    user_id: int,
) -> User | None:
    response = requests.get(f"https://example.com/users/{user_id}")
    response.text
    user = Session.get(User, user_id)
    return user


def create_user(
    user_create: UserCreateSchema,
) -> User:
    user = User(**user_create.model_dump())
    Session.add(user)
    Session.commit()
    return user
