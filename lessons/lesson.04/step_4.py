def render_user(username, address=''):
    result = f'User {username} ({address})'
    if not address:
        result = f'User {username}'

    return result, username


user_1, _ = render_user('Ivan')
# user_1, _ = render_user('Ivan', 'Moscow')
print(user_1)
# user, created = User.get_or_create(username)
