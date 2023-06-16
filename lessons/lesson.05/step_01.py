"""
инкапсуляция
наследование
полиморфизм
+ абстракция
"""


def get_user():
    return {
        "name": "Sam",
        "age": 18,
    }


def increase_age(user_data):
    user_data["age"] = user_data["age"] + 1


user = get_user()
print(user)
increase_age(user)
print(user)

print(type(user))
print(type(user).mro())

print(object)
user = object()
print(user)
# user.age = 18
