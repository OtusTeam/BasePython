import sys

nums_qty = 10  # memory O(1)

# gen expr
nums = (el for el in range(nums_qty))  # memory O(1)

print(nums)
print(next(nums))
print(next(nums))
print(next(nums))
# print(sys.getsizeof(nums))
# nums_sum = sum(nums)
# print(nums_sum)
# IOPS
nums = (el for el in range(nums_qty))
# while True:
#     try:
#         print(next(nums))
#     except StopIteration:
#         break

# print(*nums)
for el in nums:
    print(f'num = {el}')

# print('next', next(nums))
print('once again')
for el in nums:
    print(f'num = {el}')

# iterator VS generator
# nums.send()
# nums.close()
# nums.throw()
