class User:
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

    @classmethod
    def _clean_age(cls, value):
        return int(value)

    def set_older(self):
        self._age += 1


# User.set_older()
# User._clean_age(15)

class AdminUser(User):
    MIN_AGE = 25

    @classmethod
    def _clean_age(cls, value):
        _age = User._clean_age(value)

        if _age < cls.MIN_AGE:
            raise ValueError('too young')

        return _age


# print(vars(AdminUser))


class StaffUser(AdminUser):
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
