def render_user(**kwargs):
    return ', '.join({
        f'{k}={v}' for k, v in sorted(kwargs.items())
    })


print(render_user(name='Peter', age=25))

user = {
    'name': 'Ivan',
    'age': 28
}
user_profile = {
    'address': 'Moscow',
    'hobby': 'snowboard'
}
print(user)
print(render_user(**user))
user_data = user | user_profile
print(user_data)
