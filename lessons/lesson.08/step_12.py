class User:
    MIN_AGE = None

    def __init__(self, name, age, address=None):
        self.name = name
        # self.__age -> private
        # self._age -> protected
        self._age = self._clean_age(age)
        self.address = address

    @property
    def age(self):
        # if self._age is None:
        #     ...
        #     self._age = ...
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._clean_age(value)

    @staticmethod
    def _age_converter(value):
        return int(value)

    @classmethod
    def _clean_age(cls, value):
        age = cls._age_converter(value)

        if cls.MIN_AGE and age < cls.MIN_AGE:
            raise ValueError('too young')

        return age

    def set_older(self):
        self._age += 1

    def __add__(self, other):
        return self.__class__(
            self.name + other.name,
            self.age + other.age,
        )

    # def add(self, other):
    #     ...
    # def __len__(self) -> int:
    #     return len(self.name)

    def __str__(self) -> str:
        return f'{self.name} ({self.age})'

    # __repr__ = __str__


class AdminUser(User):
    MIN_AGE = 25

    @staticmethod
    def _age_converter(value):
        return float(value)


class StaffUser(User):
    MIN_AGE = 30


user_1 = User('Ivan', '18')
user_2 = AdminUser('Boris', '25')

user_3 = user_1 + user_2
# print(vars(user_3))
print(user_3)
