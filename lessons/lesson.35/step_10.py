import numpy as np


nums = np.array([1, 2, 3, 4])
nums_2 = np.array([5, 6, 7, 8])
nums_sum = nums + nums_2
nums_sub = nums - nums_2
nums_mul = nums * nums_2
print(nums_sum)
print(nums_sub)
print(nums_mul)

nums_3 = np.append(nums, [9, 10])
print(nums_3)
