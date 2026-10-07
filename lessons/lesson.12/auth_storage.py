from dataclasses import dataclass, field
from uuid import uuid4

import errors

# from user import User, hash_password
from models import User, hash_password


@dataclass(frozen=True)
class AuthStorage:
    _users: dict[str, User] = field(default_factory=dict)

    def register_user(self, username: str, new_password: str) -> User:
        if username in self._users:
            raise errors.UserAlreadyExistsError(username)

        user = User(id=uuid4(), username=username)
        user.password = new_password
        self._users[username] = user
        return user

    def login_user(self, username: str, raw_password: str) -> User:
        if not (
            (user := self._users.get(username)) is not None
            and user.password == hash_password(raw_password)
        ):
            raise errors.InvalidUsernameOrPassword

        return user
