# from abc import ABC, abstractmethod
class User:
    MIN_AGE = None

    def __init__(self, name, age, address=None):
        self.name = name
        self._age = self._clean_age(age)
        self.address = address

    @property
    def age(self):
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


class AdminUser(User):
    MIN_AGE = 25

    @staticmethod
    def _age_converter(value):
        return float(value)


class StaffUser(User):
    MIN_AGE = 30


# user_1 = User('Ivan', '18')
# user_1 = AdminUser('Ivan', '25')
user_1 = StaffUser('Ivan', '30')

print(type(user_1))
print(user_1.age)
# user_1.age = '27'
# user_1.age = '18'
# user_1.age = '27 years'
print(user_1.age)
