import sys

nums_qty = 10  # memory O(1)

nums = [el for el in range(nums_qty)]  # memory O(n)

# nums = []
# for el in range(100):
#     nums.append(el)

print(nums)
print(type(nums))
print(nums[0])
print(nums[3:5])
# print(sys.getsizeof(nums))
# nums_sum = sum(nums)
# print(nums_sum)
