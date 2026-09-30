import logging

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User

log = logging.getLogger(__name__)


class Crud:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_users(self) -> list[User]:
        stmt = select(User).order_by(User.id)
        users = self.session.scalars(stmt)
        return list(users.all())

    def get_user(self, user_id: int) -> User | None:
        response = requests.post(
            f"http://localhost:5050/api/users/{user_id}",
            json={"user_id": user_id},
        )
        user_data = response.json()
        log.debug("user %d data: %s", user_id, user_data)

        return self.session.get(User, user_id)
