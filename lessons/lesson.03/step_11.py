import time
from functools import wraps


def log_time(logger=print, threshold=1):
    def inner(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.monotonic()
            result = func(*args, **kwargs)
            end = time.monotonic()
            t_delta = end - start
            if t_delta > threshold:
                logger(f'{func.__name__}: {t_delta} sec')
            return result

        return wrapper

    return inner


def my_print(*args):
    for el in args:
        print(el, '!!!', end='')
    print()


# @log_time()
@log_time(my_print)
def make_hello(name):
    """Build hello phrase"""
    return f'{name}, hello!'


print(make_hello('Ivan'))
