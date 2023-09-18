class User:
    def __init__(self, name, age=None):  # __new__()  -> self
        self.name = name
        self.age = age
        self.address = None


user_1 = User(name='Ivan')
user_2 = User('Olga', 19)
user_3 = User(age=25, name='Oleg')
print(type(user_1))
print(user_1, user_2, user_3)
print(vars(user_1))
print(vars(user_2))
# print(dir(user_1))
