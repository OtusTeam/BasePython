"""
Create
Read
Update
Delete
"""
from pydantic import BaseModel

from .schemas import User, UserIn


class Storage(BaseModel):
    users: dict[int, User] = {}
    users_by_token: dict[str, User] = {}
    last_id: int = 0

    @property
    def next_id(self):
        self.last_id += 1
        return self.last_id

    def create_user(self, username: str) -> User:
        user = User(id=self.next_id, username=username)
        self.users[user.id] = user
        self.users_by_token[user.token] = user
        return user


storage = Storage()

storage.create_user("john")
storage.create_user("sam")
storage.create_user("bob")


def get_users() -> list[User]:
    return list(storage.users.values())


def create_user(user_in: UserIn) -> User:
    user = storage.create_user(**user_in.model_dump())
    return user


def get_user_by_id(user_id: int) -> User | None:
    return storage.users.get(user_id)


def get_user_by_token(token: str) -> User | None:
    return storage.users_by_token.get(token)

