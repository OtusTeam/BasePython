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

log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: Session):
        self.session = session

    def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = self.session.scalars(stmt)
        return list(users.all())

    def get_user(self, user_id: int) -> User | None:
        response = requests.post(
            url=f"http://127.0.0.1:5050/api/{user_id}",
            json={"foo": "bar", "user_id": user_id},
        )
        log.debug("response: %s", response.json())
        return self.session.get(User, user_id)
