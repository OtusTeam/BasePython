# Синтаксический сахар, позволяющий изменять поведение функции
from time import time
from functools import wraps


# def square_nums(nums):
#     start = time()
#     for i in nums:
#         print(i ** 2)
#     end = time()
#     print("time to complete: ", end - start)


# square_nums([1, 2, 3, 4])


# def dumb_func():
#     print("I am a dumb func")


def time_func(func):

    def inner_func(*args, **kwargs):
        print(func.__name__)
        print("function start with args: ", args, "kwargs:", kwargs)
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("function is processed in ", end - start)
        return result

    return inner_func


# def find_num(nums, num):
#     for i in nums:
#         if num == i:
#             return True
#     return False
#
#

def square_nums(nums):
    for i in nums:
        print(i ** 2)


# square_nums([1, 2])

f = time_func(square_nums)
print(f([1, 2]))

# square_nums_f = time_func(square_nums)
# square_nums_f([1, 10])
#
# square_nums(['num', 'numnum'])


# f([1, 2, 3, 4])


#
#
# def find_num(nums, num):
#     for i in nums:
#         if num == i:
#             return True
#     return False
#
#

# def dumb_func():
#     print("I am a dumb func")


# def time_func(func, test_text=None):
#     print(test_text)
#
#     def inner_func(*args, **kwargs):
#         # print(test_text)
#         print("function start with args: ", args, "kwargs:", kwargs)
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print("function is processed in ", end - start)
#         return result
#
#     return inner_func


# @time_func(test_text="test")
# def test():
#     print("test")


# f = time_func(find_num)
# print(type(f))
# print(f([1, 2, 3, 4], 1))
# f([1, 2, 3, 4])

# square_nums_f = time_func(square_nums)
# square_nums_f([1, 2, 3, 4])

# @time_func
# def square_nums(nums):
#     for i in nums:
#         print(i ** 2)
#
#
# square_nums([1, 10])

#
# @time_func
# def find_num(nums, num):
#     for i in nums:
#         if num == i:
#             return True
#     return False
#
#
# @time_func
# def process_nums(sample_nums, e=2):
#     return [num ** e for num in sample_nums]

# print(process_nums([1, 2, 4, 5]))
# print(find_num([1, 2, 3, 4], 1))
# square_nums([1, 2, 3, 4])


# @time_func
# def test():
#     print("test")


# f = time_func(test)
# f("test")

# f = time_func(find_num, "test")
# print(f([1, 2, 3, 4], 1))

# def wrapper(test="test"):
#     print(test)
#     def time_func(func):
#
#         @wraps(func)
#         def inner_func(*args, **kwargs):
#             print("function start with args: ", args, "kwargs:", kwargs)
#             start = time()
#             result = func(*args, **kwargs)
#             end = time()
#             print("function is processed in ", end - start)
#             return result
#         return inner_func
#     return time_func
#
#
# @wrapper()
# def cube(n):
#     return n*n*n
#
# cube(3)
#
# def trace(sep="-", multiplier=2):
#     def decorator(func):
#         func.level = 0
#
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             func_str = f"{func.__name__}{args}"
#             func.level += 1
#
#             print(sep * func.level * multiplier, ">", func_str)
#             result = func(*args, **kwargs)
#             print(sep * func.level * multiplier, "<", func_str, "with result", result)
#             func.level -= 1
#
#             return result
#
#         return wrapper
#
#     return decorator
