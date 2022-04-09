import numpy as np

from memory_profiler import profile

MAX_NUM = 10 ** 6 + 1


@profile
def classic_case():
    nums = [el for el in range(MAX_NUM)]
    print(type(nums), sum(nums))


@profile
def np_case():
    nums = np.arange(MAX_NUM)
    print(type(nums), nums.sum())


classic_case()
np_case()
