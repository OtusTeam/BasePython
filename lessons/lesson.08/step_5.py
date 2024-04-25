def _set_age(value):
    return int(value)


class User:
    def __init__(self, name, age, address=None):
        self.name = name
        self._age = _set_age(age)
        self.address = address

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = _set_age(value)

    # def _set_age(self, value):
    #     # self???
    #     return int(value)

    def set_older(self):
        self._age += 1


# class AdminUser(User):
#     MIN_AGE = 25
#
#     def _set_age(self, value):
#         _age = super()._set_age(value)
#
#         if _age < self.MIN_AGE:
#             raise ValueError('too young')
#
#         return _age


user_1 = User('Ivan', '18')
# user_1 = AdminUser('Ivan', '25')

print(type(user_1))
print(user_1.age)
# user_1.age = '27'
# user_1.age = '18'
# user_1.age = '27 years'
print(user_1.age)
