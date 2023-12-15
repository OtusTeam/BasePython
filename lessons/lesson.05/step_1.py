class User:
    # pass
    def __init__(self):
        self.name = None
        self.age = None


# __new__ -> self
user_3 = {
    'name': 'Ivan',
    'age': 25,
}
user_4 = {
    'name': 'Petr',
    'age': 33,
}


user_1 = User()
user_2 = User()
# print(User)
print(user_1)
# print(user_1.__dict__)
print(vars(user_1))
# print(user_2)
# print(user_3)
# print(user_4)
