def _clear_age(value):
    return int(value)


class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self.clear_age(age)
        # self._age = _clear_age(age)

    @staticmethod
    def clear_age(value):
        # ? self
        return int(value)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self.clear_age(value)
        # self._age = _clear_age(value)

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return self.full_name


class CustomUser(User):
    pass


user_john = User("John", "Doe", '25')
user_john.age = '28'
user_john.inc_age()
print(user_john)
# User.inc_age()
print(User.clear_age('33'))
