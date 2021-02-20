import numpy as np

# nums = np.arange(1, 11)
# nums_by_ten = nums.reshape((-1, 2, 10))
# print(nums_by_ten)
# nums_flat = nums_by_ten.reshape(-1)
# print(nums_flat)
# nums = np.arange(1, 10.4736842, 0.47368421)
# print(len(nums), nums)
#
# nums_2 = np.linspace(1, 10, 20)
# print(len(nums_2), nums_2)


def my_f(x, y):
    # print(x.dtype)
    return x ** 2 + y + 1


# x = np.linspace(1, 10, 10)
# y = np.linspace(1, 5, 10)
z = np.fromfunction(my_f, (10, 5))
# print(my_f(9, 4))
print(z)

# e_arr = np.empty((4, 5))
# e_arr = np.empty((4, 5), dtype=np.uint16)
# e_arr = np.zeros((4, 5), dtype=np.uint16)
# print(e_arr, e_arr.dtype)

