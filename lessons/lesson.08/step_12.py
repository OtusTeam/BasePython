class User:
    MIN_AGE = 18

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self._clear_age(age)

    @classmethod
    def create_caps(cls, first_name, last_name, age):
        return cls(first_name.upper(), last_name.upper(), age)

    @classmethod
    def _clear_age(cls, value):
        value = int(value)
        if value < cls.MIN_AGE:
            raise ValueError('age is too small')

        return value

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._clear_age(value)

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return (
            f'{self.__class__.__name__}: {self.full_name} '
            f'(min age {self.MIN_AGE})'
        )

    def __add__(self, other):
        return self.__class__(
            self.first_name + other.first_name,
            self.last_name + other.last_name,
            self.age + other.age,
        )


class CustomUser(User):
    pass


user_1 = User("John", "Doe", '18')
user_2 = CustomUser("Ivan", "Ivanov", '28')
# print(user_1)
# print(user_2)

print(dir(User))

users = user_1 + user_2
print(users)
