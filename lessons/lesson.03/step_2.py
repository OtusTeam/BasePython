def get_user_data(username):
    return 'login', 25, 'Moscow'


user_login, user_age, user_city, *others = get_user_data('Ivan')
# user_login, user_age, user_city = 'login', 25, 'Moscow'
print(user_login, user_age, user_city)
print(others)
