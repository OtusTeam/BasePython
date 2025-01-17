"""
Create
Read
Update
Delete
"""

from pydantic import BaseModel

from .schemas import (
    User,
    UserCreate,
    UserIdType,
)


class UsersStorage(BaseModel):
    users: dict[UserIdType, User] = {}
    users_by_token: dict[str, User] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create(self, user_in: UserCreate) -> User:
        user = User(
            id=self.next_id,
            **user_in.model_dump(),
        )
        self.users[user.id] = user
        self.users_by_token[user.token] = user
        return user

    def get(self) -> list[User]:
        return list(self.users.values())

    def get_by_id(self, user_id: UserIdType) -> User | None:
        return self.users.get(user_id)

    def get_by_token(self, token: str) -> User | None:
        return self.users_by_token.get(token)


storage = UsersStorage()
storage.create(
    UserCreate(
        username="sam",
        email="sam@example.com",
    ),
)
storage.create(
    UserCreate(
        username="john",
        email="john@example.com",
    ),
)
storage.create(
    UserCreate(
        username="alice",
        email="alice@example.com",
    ),
)
