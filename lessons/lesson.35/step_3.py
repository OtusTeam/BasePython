import numpy as np

from decorators import time_prof

MAX_NUM = 10 ** 5


@time_prof
def classic_python():
    nums = [el for el in range(MAX_NUM)]
    print(len(nums))


@time_prof
def numpy_python():
    nums = np.arange(MAX_NUM)
    print(len(nums))


classic_python()
numpy_python()
