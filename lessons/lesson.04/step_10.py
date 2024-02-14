import time


def profile_it(func):
    def inner(username):
        start = time.monotonic()

        result = func(username)

        end = time.monotonic()
        print(f'{end - start} sec')

        return result

    return inner


# @profile_it
def render_user(username):
    """ Render user to text """
    result = f'User {username}'

    return result


user_1 = render_user('Ivan')
# user_1 = profile_it(render_user)('Ivan')
# user_1 = inner('Ivan')

# user_1 = inner('Ivan')
print(user_1)
# print(render_user.__name__)
print(render_user.__doc__)
