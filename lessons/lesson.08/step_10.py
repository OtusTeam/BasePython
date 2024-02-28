# a = 5
#
#
# def my_func():
#     # a = 15
#     # LEGB
#     print(a)
#
#
# my_func()

# MIN_AGE = -5


class User:
    MIN_AGE = 18  # class attr  User.MIN_AGE

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name  # instance attr
        self.last_name = last_name
        self._age = self._clear_age(age)
        # self.MIN_AGE = 122
        # print(self.MIN_AGE)
        # print(User.MIN_AGE)
        # print(MIN_AGE)

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


class CustomUser(User):
    pass


user_1 = User("John", "Doe", '18')
user_2 = CustomUser("Ivan", "Ivanov", '28')
print(user_1)
print(user_2)
print(vars(User))
print(vars(user_1))
# print(User.__dict__)
print(User.MIN_AGE)
