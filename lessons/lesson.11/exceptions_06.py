from dataclasses import dataclass


class AppError(Exception):
    pass


class UserError(AppError):
    def __init__(self, username: str) -> None:
        self.username = username
        super().__init__(username)


class UserNotFoundError(UserError):
    pass


@dataclass
class User:
    username: str


users = [
    User("john"),
    User("bob"),
]

users_storage = {user.username: user for user in users}


@dataclass
class UserFetcher:
    connection: str

    def one_or_none(self, username: str) -> User | None:
        print("fetch", username, "via conn", self.connection)
        return users_storage.get(username)

    def one(self, username: str) -> User:
        user = self.one_or_none(username)
        if user:
            return user
        raise UserNotFoundError(username)

    def close(self) -> None:
        print("closing connection", self.connection)


def single_fetch(
    username: str,
    connection: str = "data://users-default",
) -> User:
    fetcher = UserFetcher(connection)

    try:
        user = fetcher.one(username)
    except UserNotFoundError as e:
        print("not found", e.username)
        raise
    else:
        print("found", user.username)
        return user
    finally:
        print(" !! finally !! ")
        fetcher.close()


def main():
    fetcher = UserFetcher("data://users")
    john = fetcher.one("john")
    print(john)

    sam = fetcher.one_or_none("sam")
    print("sam:", sam)

    user = single_fetch("bob")
    print("user:", user)


if __name__ == "__main__":
    main()
