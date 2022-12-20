def user_greet(username):
    """
    Great the user
    :param username:
    :return:
    """
    print(f'Hi, {username}!!!')


def users_greet(users):
    """

    :param users:
    :return:
    """
    for el in users:
        user_greet(el)


print(user_greet)  # callback
# print(dir(user_greet))  # callback
print(user_greet.__name__)  # callback
print(user_greet.__doc__)  # callback
print(user_greet(''))  # call
