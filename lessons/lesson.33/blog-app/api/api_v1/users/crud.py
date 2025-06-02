"""
Users CRUD

Create
Read
Update
Delete
"""

import logging
import random

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas.user import UserCreateSchema

API_URL = "http://0.0.0.0:8888/reverse-id"

log = logging.getLogger(__name__)


class UsersCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        return list(self.session.scalars(stmt).all())

    @classmethod
    def fetch_user_info(cls, user_id: int) -> None:
        response = requests.post(API_URL, json={"user_id": user_id})
        log.debug("Response: %s", response.json())

    def get_by_id(self, user_id: int) -> User | None:
        self.fetch_user_info(user_id)
        return self.session.get(User, user_id)

    def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def crete_n_users(self, n_users: int) -> list[User]:
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
