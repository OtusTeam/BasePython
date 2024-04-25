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

    def _clean_age(self, value):
        age = int(value)
        if self.MIN_AGE and age < self.MIN_AGE:
        # if self.__class__.MIN_AGE and age < self.__class__.MIN_AGE:
            raise ValueError('too young')

        return age

    def set_older(self):
        self._age += 1


class AdminUser(User):
    MIN_AGE = 25


class StaffUser(AdminUser):
    MIN_AGE = 30


# user_1 = User('Ivan', '18')
user_1 = AdminUser('Ivan', '25')
# user_1 = StaffUser('Ivan', '30')

print(type(user_1))
print(user_1.age)
# user_1.age = '27'
# user_1.age = '18'
# user_1.age = '27 years'
print(user_1.age)

print(vars(AdminUser))
print(vars(user_1))
