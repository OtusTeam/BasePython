import time


def profile(func):
    def inner(*args, **kwargs):
        start = time.monotonic()

        result = func(*args, **kwargs)

        finish = time.monotonic()
        print(f'{func.__name__}: {finish - start} sec')

        return result

    return inner


# @profile
def sqr(a):
    """ Calc sqr of a number """
    return a ** 2


# print(sqr(2))
print(f'{sqr.__name__=}')
print(help(sqr))
print(sqr.__doc__)