import numpy as np
from utils import time_prof

NUMS_QTY = 10 ** 7


@time_prof
def nums_as_list():
    nums = [num for num in range(NUMS_QTY)]
    print(type(nums), nums[-1], sum(nums))


@time_prof
def nums_as_array():
    # nums = np.arange(NUMS_QTY)
    nums = np.arange(NUMS_QTY, dtype=np.int64)
    # print(type(nums), nums[-1], sum(nums), nums.dtype)
    # print(type(nums), nums[-1], np.sum(nums), nums.dtype)
    print(type(nums), nums[-1], nums.sum(), nums.dtype)


nums_as_list()
nums_as_array()
