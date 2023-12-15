class User:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age


def set_older(user, age_diff=1):
    user['age'] += age_diff
    return user


user_3 = {
    'name': 'Ivan',
    'age': 25,
}
user_4 = {
    'name': 'Petr',
    # 'age': 33,
}

user_1 = User('Vlad', 38)
user_2 = User()
# print(User)
print(user_1)
print(vars(user_1))
# print(user_2)
# print(user_3)

user_4 = set_older(user_4)
# user_4 = check_name(user_4)

print(user_4)
