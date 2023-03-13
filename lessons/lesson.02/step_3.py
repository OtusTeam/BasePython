# DRY
# global scope
users = ['i.ivanov', 'a.andreeev', 's.sergeev']
# user = 'Ivan'


def say_hello(user_name):
    print('hello', user_name, 'have a good day!')


def greet_users():  # bad idea
    # local scope
    # user = 'Ivan'
    # print(user)
    for user_name in users:
        say_hello(user_name)


# users = ['i.ivanov', 'a.andreeev']
greet_users()
# print(user)
