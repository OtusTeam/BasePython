def get_user_data(username):
    return 'login', 25, 'Moscow', 'junior'


def say_hello(greeting, name, *args, **kwargs):
    pass


user_login, user_age, user_city, *_ = get_user_data('Ivan')
print(user_login, user_age, user_city)
print(_)
print(*_)

# for _ in range(5):
#     pass
