print('start')


def user_greet(username):
    print(f'Hello, {username}!!!')


users = ['Ivan', 'Olga', 'Nikolay', 'Igor', 'Ivan']
for el in users:
    user_greet(el)  # call func

users = ['Henry', 'Bob', 'Elena', 'Kirill']
for el in users:
    user_greet(el)
