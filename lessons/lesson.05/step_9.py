class User:
    def __init__(self, age):
        self._age = int(age)

    def get_address(self):
        pass

    def get_age(self):
        return self._age

    def set_age(self, age):
        # assert isinstance(age, int), f'wrong type of age: {type(age)}'
        self._age = int(age)

    def _get_salary(self, start_date, end_date):  # protected
        pass

    def year_older(self):
        self._age += 1


# class AdminUser(User):
#     pass


user_1 = User('25')

print(vars(user_1))
print(user_1.__dict__)
# print(user_1.age)
print(user_1.get_age())
# user_1.set_age('25 years')
user_1.set_age('25')
user_1.age = '25 years'
user_1.year_older()
print(user_1.get_age())
print(vars(user_1))

