import numpy as np
from memory_profiler import profile

from utils import time_prof

NUMS = 10 ** 6


# @profile
@time_prof
def list_case():
    nums = [num for num in range(NUMS)]
    print(type(nums), len(nums), nums[-1])


# @profile
@time_prof
def np_case():
    nums = np.arange(NUMS)
    print(type(nums), len(nums), nums[-1], nums.dtype)


if __name__ == '__main__':
    list_case()
    np_case()
