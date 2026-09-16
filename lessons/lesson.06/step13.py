# map()
# filter()

# nums = ['1', '2', '3', '5', '6', '7']
# new_list = map(int, nums)
# print(list(new_list))


# def is_even(x):
#     return x % 2 == 0
#
# nums = [1, 2, 3, 4, 5, 6, 7]
# new_list = filter(is_even, nums)
# print(list(new_list))



# nums = [1, 2, 3, 4, 5, 6, 7]
# new_list = filter(lambda x: x % 2 != 0, nums)
# print(list(new_list))



my_func = lambda x: x % 2 != 0

nums = [1, 2, 3, 4, 5, 6, 7]
new_list = filter(my_func, nums)
print(list(new_list))