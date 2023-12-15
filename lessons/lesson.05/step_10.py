class User:
    verbose_name = 'users'

    def __init__(self, name, age=None):
        self.name = name
        self._age = self._validate_age(age)
        # print(self.verbose_name)

    def _validate_age(self, age):
        return int(age)

    # def age_getter(self):
    #     return self._age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = self._validate_age(value)

    def set_older(self):
        self._age += 1


class AdminUser(User):
    verbose_name = 'admins'

    def set_older(self, age_diff=1):
        # super().set_older()
        self._age += int(age_diff)


user_1 = User('Vlad', '38')
user_2 = AdminUser('Oleg', 29)

# user_2.age = 33
user_2.age = '33'
# user_2.age = '33 years'

print(vars(user_1), type(user_1))
print(vars(user_2), type(user_2))

# users = [user_1, user_2]
# for user in users:
#     print(user.age)
print(vars(user_1))
print(vars(User))
print(user_1.verbose_name)
