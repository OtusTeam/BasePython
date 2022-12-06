def user_greet(username, punct, greeting='Hi'):
    print(f'{greeting}, {username}{punct}')


user_greet('Ivan', '!!!')
# user_greet('Ivan', 'Привет')
user_greet('Ivan', '!', greeting='Привет')
