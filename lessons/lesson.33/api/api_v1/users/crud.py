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
from schemas.user import UserCreateSchema


log = logging.getLogger(__name__)


class UsersCRUD:

    def __init__(self, session: Session) -> None:
        self.session = session

    def get_list(self) -> list[User]:
        statement = select(User).order_by(User.id)
        result = self.session.scalars(statement)
        return list(result.all())

    def get_by_id(self, user_id: int) -> User | None:
        response = requests.post(f"http://0.0.0.0:5050/api/users/{user_id}/")
        user_data = response.json()
        log.debug("User data: %s", user_data)
        return self.session.get(User, user_id)

    def create(self, user_in: UserCreateSchema) -> User:
        user = User(**user_in.model_dump())
        self.session.add(user)
        self.session.commit()
        return user
