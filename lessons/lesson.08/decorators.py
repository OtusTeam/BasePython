# Синтаксический сахар, позволяющий изменять поведение функции
from time import time


# def square_nums(nums):
#     start = time()
#     for i in nums:
#         print(i**2)
#     end = time()
#     print("time to complete: ", end - start)


# square_nums([1, 2, 3, 4])

# def square_nums(nums):
#     for i in nums:
#         print(i**2)
#
#
def find_num(nums, num):
    for i in nums:
        if num == i:
            return True
    return False


def time_func(func, test_text=None):
    print(test_text)
    def inner_func(*args, **kwargs):
        print("function start with args: ", args, "kwargs:", kwargs)
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print("function is processed in ", end-start)
        return result
    return inner_func


# f = time_func(find_num)
# print(type(f))
# print(f([1, 2, 3, 4], 1))
# f([1, 2, 3, 4])

# square_nums_f = time_func(square_nums)
# square_nums_f([1, 2, 3, 4])

# @time_func
# def square_nums(nums):
#     for i in nums:
#         print(i**2)
#
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
# print(find_num([1, 2, 3, 4], 0))
# square_nums([1, 2, 3, 4])

# @time_func(test_text="test")
# def test():
#     print("test")


# test()

f = time_func(find_num, "test")
print(f([1, 2, 3, 4], 1))
