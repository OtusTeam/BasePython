class User:
    def __init__(self, username: str) -> None:
        # self.username = f"username:{username}"
        self.username = username

    def read(self) -> dict:
        return {
            "data": f"some-user-data-{self.username}",
        }

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(username={self.username!r})"


class Manager(User):

    def __init__(
        self,
        username: str,
        email: str | None = None,
    ) -> None:
        super().__init__(username)
        self.email = email

    def read(self) -> dict:
        data = super().read()
        data.update(
            {
                "manager-username": self.username,
                "manager-email": self.email,
            },
        )
        return data

    def write(self, value):
        print(self, "write", value)


bob = User("bob")
john = Manager("john")
print(bob)
print(john)

print(bob.read())
print(john.read())
john.write("data")


def some_user_creator[U: User](user_cls: type[U], username: str) -> U:
    return user_cls(username=f"foo:{username}")


kate = some_user_creator(User, "kate")
print(kate)
print(kate.read())
kyle = some_user_creator(Manager, "kyle")
print(kyle)
print(kyle.read())
kyle.write("data")
