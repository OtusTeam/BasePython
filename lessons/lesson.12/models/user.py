__all__ = (
    "hash_password",
    "User",
)

from dataclasses import dataclass
from hashlib import sha256
from uuid import UUID, uuid4

from models.post import Post


def hash_password(raw_password: str) -> str:
    return sha256(raw_password.encode()).hexdigest()


@dataclass
class User:
    id: UUID
    username: str
    _password: str = ""

    @property
    def password(self) -> str:
        return self._password

    @password.setter
    def password(self, raw_password: str) -> None:
        self._password = hash_password(raw_password)

    def add_post(self, title: str, body: str) -> Post:
        post = Post(id=uuid4(), title=title, body=body)
        post.add_user(self)
        return post
