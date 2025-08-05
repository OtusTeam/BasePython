import logging
import random

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
        return list(self.session.scalars(statement).all())

    def get_by_id(self, user_id: int) -> User | None:
        return self.session.get(User, user_id)

    def create(self, user_create: UserCreateSchema) -> User:
        user = User(**user_create.model_dump())
        self.session.add(user)
        self.session.commit()
        return user

    def create_many(self, n_users: int) -> list[User]:
        rnd_val = random.randint(100, 1000)
        users = [
            User(
                username=f"user-{idx:03d}-{rnd_val}",
                email=f"user.{idx:03d}.{rnd_val}@site.com",
            )
            for idx in range(1, n_users + 1)
        ]
        self.session.add_all(users)
        self.session.commit()
        return users
