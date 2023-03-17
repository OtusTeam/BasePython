class User:
    # def __init__(self, age, *args, **kwargs):
    def __init__(self):
        # self.age = age
        self.age = None

    def get_address(self):
        pass

    def get_age(self):
        pass

    def _get_salary(self, start_date, end_date):  # protected
        pass

    def year_older(self):
        self.age += 1


# class AdminUser(User):
#     pass


# user_1 = User(25, name='Ivan')
# user_1 = User(25)
user_1 = User()
# user_1.age = 25
print(vars(user_1))
print(user_1.__dict__)
print(user_1.age)
user_1.year_older()
# user_1.age += 1
#
# print(user_1.age)

# user_2 = User()
# user_3 = User()
