from dataclasses import dataclass
from datetime import date
from typing import Optional


@dataclass
class User:
    id: int
    username: str
    email: str
    birth_date: date
    full_name: str = ""
    author: Optional["Author"] = None


@dataclass
class Author:
    id: int
    user: User


def get_user(user_id: int):
    username = "john"
    email = "johnsmith@example.com"
    birth_date = date(1987, 9, 24)
    # birth_date = "1987-09-24"
    user = User(id=user_id, username=username, email=email, birth_date=birth_date, full_name="John Smith")
    return user


def get_temperature(city: str) -> int:
    return 23


def demo_recursion():
    user = User(1, "sam", "sam@example.com", date(1987, 9, 24))
    author = Author(3, user)
    print(user)
    print(author)
    user.author = author
    print(user)
    print(author)


def main():
    demo_recursion()
    return
    user = get_user("42")
    print(user)
    print(f"User #{user.id}, username {user.username}, bd {user.birth_date}")
    print(user.full_name)


if __name__ == '__main__':
    main()
