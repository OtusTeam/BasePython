def say_hello(user_name):
    print('hello', user_name, 'have a good day!')


def greet_users(users):
    # print(id(users))
    users.append('me')  # side effects
    for user_name in users:
        say_hello(user_name)


my_users = ['i.ivanov', 'a.andreeev', 's.sergeev']
# my_users = ('i.ivanov', 'a.andreeev', 's.sergeev')
# print(id(my_users))
greet_users(my_users)
greet_users(my_users)
print(my_users)
