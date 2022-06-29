from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    age: int = None
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: list[int] = []
    active: bool = True

    def add_friend(self, friend_id: int):
        self.friends.append(friend_id)

    def increase_age(self):
        self.age += 1


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3', b'4'],
}
user = User(**external_data)
print("user.id:", user.id)
print("repr(user.signup_ts):", repr(user.signup_ts))
print("user.friends:", user.friends)
print("user.dict():", user.dict())


print(user.friends)
user.add_friend(5)
print(user.friends)

user.age = 16

print(user)
user.increase_age()
print(user)

# user.age = '123'
# print(user)

print(user.dict())
print(user.json())


u1 = User(id=1, signup_ts=user.signup_ts.now())
print(u1.signup_ts)
print(u1.signup_ts.timestamp())

u2 = User(id=2, signup_ts=1656527295)
print(u2.signup_ts)
