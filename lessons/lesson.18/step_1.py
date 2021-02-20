import numpy as np

from memory_profiler import profile

NUMS_QTY = 10 ** 5


@profile
def nums_as_list():
    nums = [num for num in range(NUMS_QTY)]
    print(type(nums), nums[-1])


@profile
def nums_as_array():
    nums = np.arange(NUMS_QTY)
    print(type(nums), nums[-1])


nums_as_list()
nums_as_array()
