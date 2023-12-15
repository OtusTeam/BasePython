class User:
    def __init__(self, name, age=None):
        self.name = name
        self._age = self._validate_age(age)

    def _validate_age(self, age):
        return int(age)

    @property
    def age(self):
        return self._age

    def set_older(self):
        self._age += 1


class AdminUser(User):
    # def __init__(self, name, age=None):
    #     super().__init__(name, age=age)
    def __init__(self, name, age=None, level=None):
        super().__init__(name, age=age)
        # self.name = name
        # self._age = self._validate_age(age)
        self.level = level


user_1 = User('Vlad', '38')
user_2 = AdminUser('Oleg', 29)

print(vars(user_1), type(user_1))
print(vars(user_2), type(user_2))
