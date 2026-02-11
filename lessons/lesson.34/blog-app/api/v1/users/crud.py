"""
Create
Read
Update
Delete
"""

import logging

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas import UserCreate


log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> list[User]:
        statement = select(User).order_by(User.id)
        users = self.session.scalars(statement).all()
        return list(users)

    def get_user(self, user_id: int) -> User | None:
        response = requests.post(
            f"http://localhost:5050/api/{user_id}",
            json={
                "user_id": user_id,
            },
        )
        data = response.json()
        log.debug("data: %s", data)
        return self.session.get(User, user_id)

    def create_user(
        self,
        user_create: UserCreate,
    ) -> User:
        user = User(
            **user_create.model_dump(),
        )
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user
