# Пример декоратора


# def sample_decorator(func):
#     def wrapper():
#         print("wrapper start")
#         func()
#         print("wrapper end")
#     return wrapper
#
#
# def say_hi():
#     print("Hi!")
#
#
# greet = sample_decorator(say_hi)
# print(type(greet))
# greet()
# print(greet)
# greet()
# sample_decorator(say_hi)()

# Синтаксический Сахар
# def sample_decorator(func):
#     def wrapper():
#         print("wrapper start")
#         func()
#         print("wrapper end")
#     return wrapper
#
#
# @sample_decorator
# def say_hi():
#     print("Hi!")

#
# say_hi()

# print(type(range(0, 5)))
#
# x = range(0, 4)
# print(next(x))
from time import time


def check_time(func, *args):
    def inner_func(*args, **kwargs):
        print('args: ', args, "  kwargs: ", kwargs)
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print('processed function {} in {}'.format(func, end - start))
        return result
    return inner_func


def demo_func():
    result = 0
    for i in range(0, 100):
        result = i ** 3
    return result


def demo_func_2(*args):
    for i in args:
        print(i)


# func = check_time(demo_func_2, 1, 2, 3, 4)
# func()
