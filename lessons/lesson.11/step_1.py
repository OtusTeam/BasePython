from functools import wraps

def log_args(func):
    # print(func.__name__)
    # def wrapper(*args, **kwargs):
    @wraps(func)
    def wrapper(*args):
        _args = ", ".join(map(str, args))
        print(f'{func.__name__}: {len(args)} - {_args}')
        result = func(*args)
        # if ...:
        #     result = func(*args)
        # else:
        #     ...
        return result

    return wrapper


@log_args
def sum_it(*args):
    """Calc sum"""
    return sum(args)


# sum_3 = log_args(sum_it)(2, 5, 7)
sum_3 = sum_it(2, 5, 7)
print(sum_3)

sum_5 = sum_it(2, 5, 7, -7, 4)
print(sum_5)

print(sum_it.__name__)
print(sum_it.__doc__)
