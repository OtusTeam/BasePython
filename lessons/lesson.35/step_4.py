import numpy as np
from memory_profiler import profile

NUMS = 10 ** 5


@profile
def list_case():
    nums = [num for num in range(NUMS)]
    print(type(nums), len(nums), nums[-1])


@profile
def np_case():
    nums = np.arange(NUMS)
    print(type(nums), len(nums), nums[-1], nums.dtype)


if __name__ == '__main__':
    list_case()
    np_case()
