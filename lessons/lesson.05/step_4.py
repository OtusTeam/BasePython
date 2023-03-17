# public
# protected
# private


class User:
    def get_address(self):
        pass

    def get_age(self):
        pass

    # def get_salary(self, t_period):
    # def get_salary(self, start_date, end_date):
    #     pass

    def _get_salary(self, start_date, end_date):  # protected
        pass

    def __get_salary(self, start_date, end_date):  # private
        pass


class AdminUser(User):
    pass


user_1 = User()
user_1_salary = user_1._get_salary()

user_2 = User()
user_3 = User()
