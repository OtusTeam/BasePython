class User:
    def __init__(self, name, age, address=None):
        self.name = name
        self._age = None
        self.address = address

        self._set_age(age)

    @property
    def age(self):  # getter
        return self._age

    @age.setter
    def age(self, value):
        self._set_age(value)

    def _set_age(self, value):
        self._age = int(value)

    def set_older(self):
        self._age += 1


class AdminUser(User):
    def _set_age(self, value):
        self._age = int(value)
        if self._age < 25:
            raise ValueError('too young')


# user_1 = User('Ivan', '18')
user_1 = AdminUser('Ivan', '25')

print(type(user_1))
print(user_1.age)
# user_1.age = '27'
user_1.age = '18'
# user_1.age = '27 years'
print(user_1.age)
