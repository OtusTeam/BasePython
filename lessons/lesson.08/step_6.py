from typing import List

from pydantic import BaseModel


# class Config:
#     frozen = True


# @dataclasses.dataclass(Config)
class User(BaseModel):
    pk: int
    name: str
    age: int = 25
    friends: List[int] = []

    def inc_age(self):
        self.age += 1

    # class Config:
    #     frozen = True


# class AdminUser(User):
#     pass

class AdminUser(BaseModel):
    pk: int
    name: str
    age: int = 25
    friends: List[int] = []


user_1 = User(pk=1, name='Ivan', age='25')
user_2 = AdminUser(pk=1, name='Ivan', age='25')
# user_2 = AdminUser(pk=1, name='Ivan', age=25, friends=[1, '2', b'3'])
print(user_1)
print([user_1, user_2])
print(user_1.name)
print(id(user_1), id(user_2))
print(user_1 == user_2)
user_1.name = 'Boris'
user_1.inc_age()
print(user_1)
user_1.friends.append(2)
print(user_1)
