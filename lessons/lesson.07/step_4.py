class User:
    def __init__(self, name, age, address=None):
        self.name = name
        # if not isinstance(age, int):
        #     raise ValueError('wrong age')
        # self.age = age
        self.age = int(age)
        self.address = address

    def set_older(self):
        # self.__dict__['age'] += 1
        self.age += 1


# user_1 = User('Ivan', 25)
user_1 = User('Ivan', '25')
# user_1 = User('Ivan', '25 years')
# print(user_1.__dict__)
print(vars(user_1))
user_1.set_older()
print(vars(user_1))
