"""
Create
Read
Update
Delete
"""

import random

from sqlalchemy import select
from sqlalchemy.orm import Session

from schemas import UserCreate
from models import User


class UsersCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get(self) -> list[User]:
        statement = select(User).order_by(User.id)
        return list(self.session.scalars(statement).all())

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def get_by_token(self, token: str) -> User | None:
        statement = select(User).where(User.token == token)
        return self.session.execute(statement).scalar_one_or_none()

    def create(self, user_in: UserCreate) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        self.session.commit()
        return user

    def create_n_users(self, n_users: int) -> list[User]:
        rnd_val = random.randint(1, n_users)
        users = [
            User(
                username=f"user-{idx:04d}-{rnd_val:04d}",
            )
            for idx in range(1, n_users + 1)
        ]
        self.session.add_all(users)
        self.session.commit()
        return users
