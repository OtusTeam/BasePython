import time


def render_user(username):
    start = time.monotonic()
    result = f'User {username}'
    end = time.monotonic()
    print(f'{end - start} sec')
    return result


user_1 = render_user('Ivan')
print(user_1)

other_func = render_user
print(render_user)
print(other_func)
print(other_func.__name__)

