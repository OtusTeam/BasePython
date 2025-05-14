from abc import ABC, abstractmethod
from typing import Protocol

import requests


class AbstractUser(Protocol):
    username: str
    email: str | None
    age: int

    def increase_age(self) -> None: ...


class User(AbstractUser):

    def __init__(self, username: str, email: str | None, age: int) -> None:
        self.username = username
        self.email = email
        self.age = age

    def increase_age(self) -> None:
        self.age += 1


class UserFetcher(ABC):
    @abstractmethod
    def fetch_users(self, count: int = 1) -> list[AbstractUser]: ...


class PlainUserFetcher(UserFetcher):
    def fetch_users(self, count: int = 1) -> list[AbstractUser]:
        return [
            User(
                username="username",
                email="user@email.com",
                age=18,
            )
            for _ in range(count)
        ]


class RandomUserFetcher(UserFetcher):
    API_URL = "https://randomuser.me/api/"

    def get_random_user(self) -> AbstractUser:
        data = requests.get(self.API_URL).json()
        user_data = data["results"][0]
        return User(
            username=user_data["login"]["username"],
            email=user_data["email"],
            age=user_data["dob"]["age"],
        )

    def fetch_users(self, count: int = 1) -> list[AbstractUser]:
        return [self.get_random_user() for _ in range(count)]


def get_and_show_users(fetcher: UserFetcher, count: int) -> None:
    users = fetcher.fetch_users(count=count)
    for user in users:
        print("@", user.username, user.email, user.age)
        user.increase_age()


def main() -> None:
    # user = User(
    #     username="username",
    #     email="user@email.com",
    #     age=18,
    # )
    # print(user)
    plain_user_fetcher = PlainUserFetcher()
    get_and_show_users(plain_user_fetcher, count=2)
    random_user_fetcher = RandomUserFetcher()
    get_and_show_users(random_user_fetcher, count=3)


if __name__ == "__main__":
    main()
