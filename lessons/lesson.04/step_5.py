def render_user(username, address=''):
    result = f'User {username} ({address})'
    if not address:
        result = f'User {username}'

    return result, username, address


# user_1, _, _ = render_user('Ivan')
_, user_1, *othr = render_user('Ivan')
print(user_1)
print(othr)
