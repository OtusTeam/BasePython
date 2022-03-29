from dataclasses import dataclass


@dataclass()
# @dataclass(frozen=True)
class User:
    pk: int
    name: str
    age: int

    def inc_age(self):
        self.age += 1


class AdminUser(User):
    pass


user_1 = User(1, 'Ivan', 25)
user_2 = AdminUser(1, 'Ivan', 25)
print(user_1)
print([user_1, user_2])
print(user_1.name)
print(id(user_1), id(user_2))
print(user_1 == user_2)
user_1.name = 'Boris'
user_1.inc_age()
print(user_1)
