from time import time


# def square_nums(nums):
#     start = time()
#     result = [num ** 2 for num in nums]
#     end = time()
#     print('Completed in {} milliseconds'.format(end - start))
#     return result
#
#
# square_nums([1, 2, 4, 5])
# square_nums(nums=[1, 2, 4, 5])
#
#
# def demo(*args, **kwargs):
#     print("args: ", args)
#     print("kwargs: ", kwargs)
#
#
# demo()
#
# demo([1, 2, 3, 4], test='test')
#
#
# def demo_func():
#     result = 0
#     for i in range(0, 100):
#         result = i ** 3
#     return result
#
#
# def demo_func_2(*args):
#     for i in args:
#         print(i)
#
#
# def check_time(func):
#     def inner_func(*args, **kwargs):
#         print(args, "  ", kwargs)
#         start = time()
#         result = func(*args, **kwargs)
#         end = time()
#         print('processed function {} in {}'.format(func, end - start))
#         return result
#
#     return inner_func
#
#
# func = check_time(demo_func)
# func_2 = check_time(demo_func_2)
#
# print(func)
# print(func_2)
# func()
# print('ok')
# func_2([1, 2, 3, 4])
#
#
# @check_time
# def demo_func_3():
#     print('test demo func 3')
#
#
# demo_func_3()
