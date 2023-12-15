class User:
    def __init__(self, name, age=None):
        self.name = name
        self._current_age = self._validate_current_age(age)

    def _validate_current_age(self, age):
        return int(age)

    @property
    def age(self):
        return self._current_age

    def set_older(self):
        self._current_age += 1


class AdminUser(User):  # mixins
    pass


user_1 = User('Vlad', '38')
user_2 = AdminUser('Oleg', 29)

print(vars(user_1), type(user_1))
print(vars(user_2), type(user_2))

if isinstance(user_2, AdminUser):
    print('granted')
