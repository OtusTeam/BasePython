from sys import getsizeof

import numpy as np
from psutil import virtual_memory
from utils import show_mem

NUMS_QTY = 10 ** 6


def nums_as_list():
    mem = virtual_memory().used
    nums = [num for num in range(NUMS_QTY)]
    print(type(nums), getsizeof(nums) / 2 ** 20, nums[-1])
    show_mem(mem)


def nums_as_array():
    mem = virtual_memory().used
    # nums = np.arange(NUMS_QTY)
    nums = np.arange(NUMS_QTY, dtype=np.int64)
    print(type(nums), getsizeof(nums) / 2 ** 20, nums[-1])
    show_mem(mem)


nums_as_list()
nums_as_array()
