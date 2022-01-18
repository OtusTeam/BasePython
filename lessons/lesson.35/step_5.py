import numpy as np

from memory_profiler import profile

MAX_NUM = 10 ** 5


@profile
# @time_prof
def classic_python():
    nums = [el for el in range(MAX_NUM)]
    print(len(nums))


@profile
# @time_prof
def numpy_python():
    nums = np.arange(MAX_NUM)
    print(len(nums))
    # print(np.sum(nums))
    # print(nums.sum())


classic_python()
numpy_python()
