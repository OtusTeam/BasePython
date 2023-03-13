def say_hello(user_name):
    print('hello', user_name, 'have a good day!')


def say_hello_with_greeting(user_name, greeting):
    print('hello', user_name, greeting)


def greet_users(users):
    for user_name in users:
        say_hello(user_name)


users = ['i.ivanov', 'a.andreeev', 's.sergeev']
# greet_users(users)
# greet_users()

say_hello('a.andreeev')
say_hello_with_greeting('a.andreeev', 'have a very good day!')
