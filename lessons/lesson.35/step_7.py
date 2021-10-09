import numpy as np

from utils import time_prof

NUMS = 10 ** 6


@time_prof
def list_case():
    nums = [num for num in range(NUMS)]
    # print(type(nums), len(nums), nums[-1])
    print(sum(nums))


@time_prof
def np_case():
    nums = np.arange(NUMS)
    # print(type(nums), len(nums), nums[-1], nums.dtype)
    # print(sum(nums))
    print(nums.sum())


if __name__ == '__main__':
    list_case()
    np_case()
