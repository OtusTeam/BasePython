from dataclasses import dataclass, asdict, field


@dataclass()
class User:
    id: int
    name: str
    email: str = None


@dataclass()
class Manager(User):
    users: list = field(default_factory=list)

    def add_managed_user(self, user):
        self.users.append(user)


def demo_user_dc():
    user = User(1, name="John")
    print(user)
    u1 = user

    user2 = User("2", "Sam", "sam@example.com")
    print(user2)
    # user3 = User(3, "Nick", email="nick@example.com", profile={"abc": "qwe"})
    user3 = User(3, "Nick", email="nick@example.com")
    print(user3)

    # u1.email = "user@example.com"
    print(user)
    help(User.__init__)
    help(User)
    print([u1, user2, user3])

    # u4_1 = User(name="U4", id=4)
    u4_1 = User(id=4, name="U4")
    u4_2 = User(**{"name": "U4", "id": 4})
    assert u4_1 == u4_2

    u5 = User(id={"spam": "eggs"}, name="Bob")
    print(u5)
    # u5.name = "Kate"
    u5.id["fizz"] = "buzz"
    print(u5)

    user_params = asdict(user3)
    print(user_params)
    manager = Manager(**user_params)
    print(manager)
    print("manager == user3", manager == user3)
    u6 = User(id=100_000**100_000, name="Jack")
    print(u6.name, u6.id > 10_000_000)
    print(10_000_000)

    value = 1000123
    num = hex(value)
    print("num hex", num)

    num_str = ''
    while value:
        value, mod = divmod(value, 10)
        print(value, mod)
        num_str = str(mod) + num_str

    print("num_str", num_str)


def main():
    demo_user_dc()


if __name__ == '__main__':
    main()
