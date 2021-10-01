from functools import wraps


# def logged(func):
#     def with_logging(*args, **kwargs):
#         print(func.__name__ + " was called")
#         return func(*args, **kwargs)
#
#     return with_logging


# @logged
# def find_num(nums, num):
#     for i in nums:
#         if num == i:
#             return True
#     return False
#
#
# find_num([1, 2, 3, 4], 1)


def logged(func):
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging

# @logged
# def f(x):
#    """does some math"""
#    return x + x * x


def f(x):
    """does some math"""
    return x + x * x

# print(f.__name__)

# func = logged(f)
# print(func.__name__)
# print(func.__doc__)


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):

        print(func.__name__ + " was called")
        return func(*args, **kwargs)

    return with_logging


@logged
def f(x):
    """does some math"""
    return x + x * x


print(f.__name__)  # prints 'f'
print(f.__doc__)  # prints 'does some math'
print(f.__module__)
