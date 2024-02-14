def render_user(username):
    result = f'User {username}'

    return result, username


user_1, _ = render_user('Ivan')
print(user_1)
# user, created = User.get_or_create(username)

data = (1, 2, 3, 'hello')
print(data)
print(*data)
# (1, 2, 3, 'hello')
# *(1, 2, 3, 'hello') -> 1, 2, 3, 'hello'
