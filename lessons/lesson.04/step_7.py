def sum_sqr(nums):
    result = 0
    for num in nums:
        result += num ** 2

    return result


print(sum_sqr([2, 3]))
print(sum_sqr([2, 3, 4]))
print(sum_sqr([2, 3, 4, 5]))
# a, b, c = [2, 3, 4]
# print(a, b, c)
a, *b = [2, 3, 4]
print(a, b)
