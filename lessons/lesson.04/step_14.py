def render_user(username, address='', age=None, **kwargs):
    print(type(kwargs))
    print(kwargs)
    if 'grade' in kwargs:
        pass

    result = (
        f'User {username} '
        f'({address or "no address"}, {age or "no age"})'
    )

    return result


# user_1 = render_user('Ivan')
# user_1 = render_user('Ivan', 'Moscow')
# user_1 = render_user('Ivan', '', 25)
# user_1 = render_user('Ivan', age=25, grade='middle')
user_1 = render_user('Ivan', age=25)
print(user_1)

params = {'username': 'Boris', 'age': 30}
user_2 = render_user(**params)
print(user_2)
