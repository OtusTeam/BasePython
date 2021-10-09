import numpy as np

nums = np.arange(1, 101, dtype=np.int32)

nums_by_ten = nums.reshape((-1, 10))
print(nums_by_ten)
print(np.linalg.det(nums_by_ten))
nums_by_ten_t = nums_by_ten.transpose()
print(nums_by_ten_t)
