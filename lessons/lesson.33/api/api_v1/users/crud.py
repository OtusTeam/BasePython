import logging

import requests
from sqlalchemy import select
from sqlalchemy.orm import Session

from models import User
from schemas.user import UserCreateSchema

log = logging.getLogger(__name__)


class UsersCRUD:
    def __init__(self, session: Session):
        self.session = session

    def get_list(self) -> list[User]:
        statement = select(User).order_by(User.id)
        result = self.session.scalars(statement)
        return list(result.all())

    def get_by_id(self, user_id: int) -> User | None:
        response = requests.get(f"http://localhost:5050/users/{user_id}")
        response_data = response.json()
        log.info("response data: %s", response_data)

        return self.session.get(User, user_id)

    def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        self.session.commit()
        # self.session.refresh(user)
        return user
