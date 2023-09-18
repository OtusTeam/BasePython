class User:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        self.address = None


class AdminUser(User):
    pass
    # def __init__(self, name, age=None):
    #     super().__init__(name, age=age)


user_1 = User(name='Ivan', age=18)
user_2 = AdminUser(name='Boris', age=25)
print(vars(user_1))
print(vars(user_2))
