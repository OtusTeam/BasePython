from datetime import datetime

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str = ...
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"


def get_user(user_id: int) -> User:
    # return User(id=user_id, username="john", email="john@example.com", created_at="2021-09-24T20:52:30")
    return User(id=user_id, username="john", email="john@example.com")


def main():
    user = get_user("42")
    print(user)


if __name__ == '__main__':
    main()
