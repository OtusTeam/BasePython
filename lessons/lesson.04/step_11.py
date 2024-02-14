import time
import functools


def profile_it(func):
    @functools.wraps(func)
    def inner(username):
        start = time.monotonic()

        result = func(username)

        end = time.monotonic()
        print(f'{end - start} sec')

        return result

    return inner


@profile_it
def render_user(username):
    """ Render user to text """
    result = f'User {username}'

    return result


user_1 = render_user('Ivan')
print(user_1)

print(render_user.__doc__)
print(render_user.__name__)
