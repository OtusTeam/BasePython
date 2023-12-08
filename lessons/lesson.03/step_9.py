import time


def profile_it(func):
    def inner(*args, **kwargs):
        start = time.monotonic()

        result = func(*args, **kwargs)

        end = time.monotonic()
        print(f'{func.__name__}{args}: {end - start}')

        return result

    return inner


# @check_access
@profile_it
def sum_squares(*args):
    return sum(el ** 2 for el in args)


# result = sum_squares(2, 3)
# result = profile_it(sum_squares)(2, 3)
# result = inner(2, 3)

print(sum_squares(2, 3))
print(sum_squares(2, 3, 5))
