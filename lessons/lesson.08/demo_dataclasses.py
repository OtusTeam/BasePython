from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    age: int
    username: str
    email: str
    full_name: str

    def increase_age(self):
        self.age += 1


def get_user():
    user_id = 42
    age = 21
    username = "john"
    email = "john@example.com"
    full_name = "John Smith"
    return User(user_id, age, username, email, full_name)


def main():
    user = get_user()
    user2 = get_user()
    print(user)
    print(user2)
    print("user.user_id", [user.user_id])
    print("user.full_name", user.full_name)
    print("equal?", user == user2)
    print("equal?", user is user2)
    # user2.age += 1
    user2.increase_age()
    print(user2)
    print("equal?", user == user2)


if __name__ == '__main__':
    main()
