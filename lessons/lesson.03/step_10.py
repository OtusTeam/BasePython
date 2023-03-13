import time
from functools import wraps


def log_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.monotonic()
        result = func(*args, **kwargs)
        end = time.monotonic()
        print(f'{func.__name__} ({id(func)}): {end - start} sec')
        return result

    return wrapper


@log_time
def make_hello(name):
    """Build hello phrase"""
    return f'{name}, hello!'


# @log_memory
@log_time
def sum_it(*args):
    print(f'sum {len(args)} nums')
    return sum(args)


result = log_time(make_hello)('Ivan')

print(make_hello('Ivan'))
print(make_hello('Ivan'))
# print(sum_it(*[el for el in range(100)]))
print(make_hello.__name__)
print(make_hello.__doc__)
print(id(make_hello))
# print(sum_it.__name__)
# print(id(sum_it))
