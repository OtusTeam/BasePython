"""
Create
Read
Update
Delete
"""

from pydantic import BaseModel

from .schemas import User, UserCreate


class Storage(BaseModel):
    users: dict[int, User] = {}
    users_by_token: dict[str, User] = {}
    last_id: int = 0

    @property
    def next_id(self) -> int:
        self.last_id += 1
        return self.last_id

    def create_user(self, user_in: UserCreate) -> User:
        user: User = User(
            id=self.next_id,
            **user_in.model_dump(),
        )
        self.users[user.id] = user
        self.users_by_token[user.token] = user
        return user

    def get_users(self) -> list[User]:
        return list(self.users.values())

    def get_user(self, user_id: int) -> User | None:
        return self.users.get(user_id)

    def get_user_by_token(self, token: str) -> User | None:
        return self.users_by_token.get(token)


storage = Storage()

storage.create_user(
    UserCreate(
        username="john",
        email="john@example.com",
    ),
)
storage.create_user(
    UserCreate(
        username="sam",
        email="sam@ya.ru",
    ),
)
storage.create_user(
    UserCreate(
        username="bob",
        email="bob@yahoo.com",
    ),
)
