def user_greet(username):
    print(f'Hi, {username}!!!')


def users_greet(users):
    for el in users:
        user_greet(el)


users = ['Ivan', 'Olga', 'Nikolay', 'Igor', 'Ivan']
users_greet(users)

users = ['Henry', 'Bob', 'Elena', 'Kirill']
users_greet(users)
