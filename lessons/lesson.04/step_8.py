def sum_sqr(*nums):
    print(type(nums))
    print(nums)

    result = 0
    for num in nums:
        result += num ** 2

    return result


print(sum_sqr(2, 3))
print(sum_sqr(2, 3, 4))
print(sum_sqr(2, 3, 4, 5))
# print(1, 2, 3, 'hello')

nums = [1, 2, 6, 7, 9, 34, 2]
# 1, 2, 6, 7, 9, 34, 2

print(sum_sqr(*nums))
print(sum_sqr(1, 2, 6, 7, 9, 34, 2))
print(sum_sqr([1, 2, 6, 7, 9, 34, 2]))
