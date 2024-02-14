import time
import functools


def profile_it(func):
    @functools.wraps(func)
    def inner(*args):
        start = time.monotonic()

        result = func(*args)

        end = time.monotonic()
        print(f'{end - start} sec')

        return result

    return inner


@profile_it
def render_user(username):
    """ Render user to text """
    result = f'User {username}'

    return result


@profile_it
def sum_sqr(*nums):
    print(type(nums))
    print(nums)

    result = 0
    for num in nums:
        result += num ** 2

    return result


# user_1 = render_user('Ivan')
# print(user_1)
#
# print(render_user.__doc__)
# print(render_user.__name__)
print(sum_sqr(2, 3))
