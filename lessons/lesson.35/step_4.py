import numpy as np

from decorators import time_prof

MAX_NUM = 10 ** 6 + 1


@time_prof
def classic_case():
    nums = [el for el in range(MAX_NUM)]
    print(type(nums), sum(nums))


@time_prof
def np_case():
    nums = np.arange(MAX_NUM)
    # print(type(nums), sum(nums))
    # print(type(nums), np.sum(nums))
    print(type(nums), nums.sum())


classic_case()
np_case()
