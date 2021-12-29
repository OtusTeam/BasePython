from datetime import datetime
# from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int
    name: str
    signup_ts: datetime = None
    # friends: list["User"] = []
    # friends: list[Optional[int]] = []
    friends: list[int] = []

    def increase_age(self):
        self.age += 1


class Food(BaseModel):
    name: str
    weight: int

    class Config:
        frozen = True


def get_user():
    user_id = 7
    user_age = 15
    some_name = "sam"
    return User(id=user_id, age=user_age, name=some_name)


def demo_food():
    milk = Food(name="milk", weight=950)
    bread = Food(name="bread", weight="300")

    print("milk:", milk)
    print("bread:", bread)

    try:
        milk.weight -= 50
    except TypeError:
        print("error")
    print("milk:", milk)


def demo_users():
    sam = User(id=1, age=20, name="Sam")
    john = User(id=2, age=22, name="John")
    print(sam)
    print(john)
    sam.friends.append(1)
    sam.friends.append(2)
    john.friends.append(3)
    john.friends.append(4)
    print(sam)
    print(john)

    nick_data = {
        "id": "7",
        "age": 42,
        "name": "Nick",
        "signup_ts": "2020-07-15T22:42:55",
        # "friends": ["1", b"2", 3, None],
        "friends": ["1", b"2", 3, ],
    }

    nick = User(**nick_data)
    print(nick)

    print(type(nick.dict()), nick.dict())
    print(type(nick.json()), nick.json())


def main():
    demo_users()
    return
    demo_food()
    user = get_user()
    print("user:", user)
    user.increase_age()
    print("user:", repr(user))
    user.increase_age()
    print("user:", [user])
    print(user.dict())
    # user.name
    # user.age


if __name__ == '__main__':
    main()
