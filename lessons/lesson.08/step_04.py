class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self._validate_age(age)  # protected

    def _validate_age(self, value):
        return int(value)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):
        return self._age

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return self.full_name


class CustomUser(User):
    @property
    def age(self):
        return f'{self._age} years'


user_john = User("John", "Doe", 25)
# user_john.age = 28
# user_john._validate_age()
print(user_john.age)
user_john.inc_age()
print(user_john)
