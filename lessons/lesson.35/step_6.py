import numpy as np
from psutil import virtual_memory

from utils import show_mem

NUMS = 10 ** 6


# @profile
# @time_prof
def list_case():
    start_mem = virtual_memory().used
    nums = [num for num in range(NUMS)]
    print(type(nums), len(nums), nums[-1])
    show_mem(start_mem)


# @profile
# @time_prof
def np_case():
    start_mem = virtual_memory().used
    nums = np.arange(NUMS)
    print(type(nums), len(nums), nums[-1], nums.dtype)
    show_mem(start_mem)


if __name__ == '__main__':
    list_case()
    np_case()
