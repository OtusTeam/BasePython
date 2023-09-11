def nums_1(n=100):
    # result = []
    # for num in range(n):
    #     result.append(num)
    # return result
    return [num for num in range(n)]  # list compr


my_nums = nums_1(10)
my_sum = sum(my_nums)
print(my_sum)
print(type(my_nums))
print(my_nums[:5])
