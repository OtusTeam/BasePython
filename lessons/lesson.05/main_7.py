def add_nums(num_1, num_2, *nums):
    print(type(nums))
    num_1, *num_2, num_3 = nums
    print(num_1, num_2, nums)
    return num_1 + num_3


my_result = add_nums(1, 2, 3, 4, 5, 6, 7)
print(my_result)
print(type(my_result))
