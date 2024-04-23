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
    MIN_AGE = 25

    def _set_age(self, value):
        # self._age = int(value)
        super()._set_age(value)

        if self._age < self.MIN_AGE:
            raise ValueError('too young')


# user_1 = User('Ivan', '18')
user_1 = AdminUser('Ivan', '18')

print(type(user_1))
print(user_1.age)
# user_1.age = '27'
# user_1.age = '18'
# user_1.age = '27 years'
print(user_1.age)
