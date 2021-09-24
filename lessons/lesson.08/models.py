from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str = ...
    created_at: datetime = Field(default_factory=datetime.now)
    status: str = "active"
    author: Optional["Author"] = None


class Author(BaseModel):
    id: int
    full_name: str
    created_at: datetime = Field(default_factory=datetime.now)
    user: User = ...


class Post(BaseModel):
    # id: int
    title: str
    body: str
    author: Author


def get_user() -> User:
    return User(id=123, username="john", email="john@example.com")


def create_author(user: User) -> Author:
    author = Author(id=1, full_name="John Smith", user=user)
    user.author = author
    return author


def create_post(title: str, body: str, author: Author) -> Post:
    post = Post(title=title, body=body, author=author)
    return post


def main():
    user = get_user()
    print(repr(user))
    author = create_author(user)
    print(repr(author))
    print(repr(user))

    post1 = create_post("Django lesson", "Today...", author)
    post2 = create_post("Flask lesson", "Today...", author)
    print(post1)
    print(post2)


if __name__ == '__main__':
    main()
