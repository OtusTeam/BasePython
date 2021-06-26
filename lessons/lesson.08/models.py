from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    username: str
    email: str
    created_at: datetime = Field(default_factory=datetime.now)
    author: Optional["Author"] = None


class Author(BaseModel):
    id: int
    full_name: str
    created_at: datetime = Field(default_factory=datetime.now)
    user: User = ...
    # user: User = Field(...)


class Post(BaseModel):
    title: str
    author: Author


def get_user():
    return User(id=1, username="john")


def create_author(user: User):
    author = Author(id=1, full_name="John Smith", user=user)
    user.author = author
    return author


def create_post(title: str, author: Author):
    return Post(title=title, author=author)


def main():
    user = get_user()
    print(repr(user))
    author = create_author(user)
    print(repr(user))
    print(repr(author))

    post1 = create_post("Django lesson", author)
    post2 = create_post("Flask lesson", author)
    print(post1)
    print(post2)


if __name__ == '__main__':
    main()
