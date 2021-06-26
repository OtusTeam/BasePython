from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    friends: List[int] = []
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"


def get_user():
    return User(id=13, username="john", friends=[1, "2"])


def main():
    user1 = get_user()
    print(repr(user1))
    # print(user1.created_at.timestamp())
    user2 = User(id=2, username="sam")
    print(user2)
    user3 = User(id=3, username="ann", created_at=1624698821)
    print(user3)
    user2.friends.append(3)
    user3.friends.append(2)
    print(user2)
    print(user3)
    print(user3.dict())
    print(user3.json())


if __name__ == '__main__':
    main()

