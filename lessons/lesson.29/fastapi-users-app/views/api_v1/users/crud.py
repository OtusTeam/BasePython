"""
Create
Read
Update
Delete
"""
import logging
from typing import Sequence

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas.user import (
    UserCreate,
    UserIdType,
)

log = logging.getLogger(__name__)


class UsersStorage:

    def __init__(self, session: Session) -> None:
        self.session = session

    def create(
        self,
        user_in: UserCreate,
    ) -> User:
        user = User(
            **user_in.model_dump(),
        )
        self.session.add(user)
        self.session.commit()
        return user

    def get(self) -> Sequence[User]:
        stmt = (
            # users
            select(User)
            # order by!
            .order_by(User.id)
        )
        return self.session.scalars(stmt).all()

    def get_by_id(self, user_id: UserIdType) -> User | None:
        response = requests.get("https://httpbin.org/get")
        # data = response.json()
        data = response.text
        log.debug("Data: %s", data)
        return self.session.get(User, user_id)

    def get_by_token(self, token: str) -> User | None:
        stmt = select(User).where(User.token == token)
        user: User | None = self.session.scalars(stmt).one_or_none()
        return user
