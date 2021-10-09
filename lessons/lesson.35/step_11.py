import numpy as np

nums = np.arange(1, 51)
print(nums, nums.shape)

# nums_by_strict = nums.reshape((5, 10))
# print(nums_by_strict, nums_by_strict.shape)

# nums_by_ten = nums.reshape((-1, 10))
# nums_by_ten = nums.reshape((10, -1))
# print(nums_by_ten)
# print(nums_by_ten.sum())
# print(nums_by_ten.sum(axis=0))
# print(nums_by_ten.sum(axis=1))
# print(nums_by_ten.prod(axis=0))
# print(nums_by_ten.prod(axis=1))

nums_3d = nums.reshape((-1, 5, 2))
print(nums_3d)
print(nums_3d.shape)
print(nums_3d[0, 0, 0])
print(nums_3d[:, 0, 0])
print(nums_3d[:, :, 0])

