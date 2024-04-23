class User:
    # pass
    def __init__(self, name, age, address=None):
        self.name = name
        self.age = age
        self.address = address


user_1 = User('Ivan', 25)
# __call__ -> __new__ -> ? __init__
# print(type(user_1))
# print(dir(user_1))
print(user_1.__dict__)
