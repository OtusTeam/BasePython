"""
CRUD functions for users

Create
Read
Update
Delete
"""
from pydantic import BaseModel

from .schemas import User, UserCreate


class Storage(BaseModel):
    users: dict[int, User] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_user(self, user_in: UserCreate) -> User:
        user = User(id=self.next_id, **user_in.model_dump())
        self.users[user.id] = user
        return user

    def get_users(self) -> list[User]:
        return list(self.users.values())

    def get_user(self, user_id: int) -> User | None:
        return self.users.get(user_id)


storage = Storage()
storage.create_user(
    UserCreate(
        username="John",
        email="john@abc.com"
    ),
)
storage.create_user(
    UserCreate(
        username="Sam",
        email="sam@yahoo.com"
    ),
)
storage.create_user(
    UserCreate(
        username="Alice",
        email="alice@yandex.ru"
    ),
)
