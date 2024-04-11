import time


def profile(func):
    def inner(*args, **kwargs):
        start = time.monotonic()

        result = func(*args, **kwargs)

        finish = time.monotonic()
        print(f'{func.__name__}: {finish - start} sec')

        return result

    return inner


@profile
def sum_sqr(a, b):
    return a ** 2 + b ** 2


@profile
def sqr(a):
    return a ** 2


print(sqr(2))

nums_1 = [2, 3]
print(sum_sqr(*nums_1))
