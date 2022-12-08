# user_input = 'Ivan Ivanov'
user_input = 'Ivan Ivanov Ivanovich'

# print(user_input.split())
# first_name = user_input.split()[0]
# last_name = user_input.split()[1]
print(user_input.split())
first_name, last_name, *_ = user_input.split()
print(first_name, last_name)
# print(_)


def user_greet(username, *args, **kwargs):
    print(args)


user_greet('Nikolay', '25', 'Moscow', 3)
user_greet('Nikolay', '25')
user_greet('Nikolay')
