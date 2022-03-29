from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel


# class Config:
#     frozen = True


# @dataclasses.dataclass(Config)
class User(BaseModel):
    pk: int
    name: str
    age: int = 25
    friends: List[int] = []
    last_login: Optional[datetime]

    def inc_age(self):
        self.age += 1

    # class Config:
    #     frozen = True


class AdminUser(User):
    pass


user_1 = User(pk=1, name='Ivan', age='25')
user_2 = AdminUser(pk=1, name='Ivan', age=25,
                   friends=[1, '2', b'3'],
                   last_login='2022-03-29T17:25')
user_2_as_dict = user_2.dict()
user_2_as_json = user_2.json()
print(user_2)
print(type(user_2_as_dict), user_2_as_dict)
print(type(user_2_as_json), user_2_as_json)
