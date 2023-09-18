class User:
    def __init__(self, name, age=None, **kwargs):
        self.name = name
        self.age = age
        self.address = None

    def show_me(self):
        print(self.name)


class AdminUser(User):
    def __init__(self, name, age=None, level=0):
        super().__init__(name, age=age, level=level)
        self.level = level

    def show_me(self):
        # super().show_me()
        print(f'me: {self.name}')


user_1 = User(name='Ivan', age=18)
user_2 = AdminUser(name='Boris', age=25, level=3)
print(vars(user_1))
print(vars(user_2))
