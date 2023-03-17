class User:
    def __init__(self, age):
        self.age = int(age)

    def get_address(self):
        pass

    def get_age(self):
        pass

    def set_age(self, age):
        self.age = int(age)

    def _get_salary(self, start_date, end_date):  # protected
        pass

    def year_older(self):
        self.age += 1


# class AdminUser(User):
#     pass


user_1 = User('25')

print(vars(user_1))
print(user_1.__dict__)
print(user_1.age)
# user_1.set_age('25 years')
user_1.set_age('25')
user_1.age = '25 years'
user_1.year_older()

