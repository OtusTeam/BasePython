# class _HiddenUser:
#     pass
#
#
# def _validate_age():
#     pass


class User:
    # class _Address():
    #     pass

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self._clear_age(age)

    def _clear_age(self, value):
        return int(value)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):  # getter
        return self._age

    @age.setter
    def age(self, value):  # setter
        self._age = self._clear_age(value)

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return self.full_name


class CustomUser(User):
    @property
    def age(self):
        origin = super().age
        return f'{origin} years'


user_john = User("John", "Doe", '25')
user_john.age = '28 years'
# user_john._validate_age()
print(user_john.age)
user_john.inc_age()
print(user_john)
