class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = self._clear_age(age)

    # def create_caps(self, first_name, last_name, age):
    #     return self.__class__(first_name.upper(), last_name.upper(), age)
    @classmethod
    def create_caps(cls, first_name, last_name, age):
        # ...
        return cls(first_name.upper(), last_name.upper(), age)

    @staticmethod
    def _clear_age(value):
        return int(value)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name} ({self._age})"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._clear_age(value)
        # self._age = _clear_age(value)

    def inc_age(self):
        self._age += 1

    def __str__(self):
        return f'{self.__class__.__name__}: {self.full_name}'


class CustomUser(User):
    pass


# user_1 = User("John", "Doe", '25')
user_1 = User.create_caps("John", "Doe", '25')
# user_2 = CustomUser("Ivan", "Ivanov", '28')
user_2 = CustomUser.create_caps("Ivan", "Ivanov", '28')
if isinstance(user_2, CustomUser):
    print('access granted')
print(user_1)
print(user_2)
