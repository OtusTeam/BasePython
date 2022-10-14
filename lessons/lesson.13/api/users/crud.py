"""
Create
Read
Update
Delete
"""
from dataclasses import dataclass, Field

from .schemas import UserIn, User


@dataclass
class UserStorage:
    counter: int
    by_id: dict[int, User]
    by_token: dict[str, User]

    @property
    def next_id(self) -> int:
        self.counter += 1
        return self.counter


storage = UserStorage(counter=0, by_id={}, by_token={})


# Get
def get_users() -> list[User]:
    return list(storage.by_id.values())


# from typing import Optional
# Optional[User]

# Get (details)
def get_user_by_id(user_id: int) -> User | None:
    return storage.by_id.get(user_id)


def get_user_by_token(token: str) -> User | None:
    return storage.by_token.get(token)


# CREATE
def create_user(user_in: UserIn) -> User:
    user = User(id=storage.next_id, **user_in.dict())
    storage.by_id[user.id] = user
    storage.by_token[user.token] = user
    return user


# Delete
def delete_user(user_id: int) -> None:
    storage.by_id.pop(user_id, None)

