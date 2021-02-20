import numpy as np

# nums = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) * 100
# percents = (1, 5, 10, 25, 50, 75, 95, 99)
# stat = np.percentile(np.abs(nums), percents)
# print(dict(zip(percents, stat)))
# print(nums)

nums = np.array([1, 2, 3, 4])
nums_2 = np.array([5, 6, 7, 8])
nums_sum = nums + nums_2
nums_sub = nums - nums_2
nums_mul = nums * nums_2
print(nums_sum)
print(nums_sub)
print(nums_mul)
