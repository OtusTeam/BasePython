def say_hello(user_name, greeting='', start_word='hello'):
# def say_hello(user_name, start_word, greeting=''):
    print(start_word, user_name, greeting)


def greet_users(users):
    for user_name in users:
        say_hello(user_name)


users = ['i.ivanov', 'a.andreeev', 's.sergeev']
# greet_users(users)
# greet_users()

say_hello('a.andreeev')
say_hello('a.andreeev', 'have a very good day!')
say_hello('a.andreeev', 'have a very good day!', 'hi')
