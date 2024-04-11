# nums = [1, 2, 3]
# print(nums)
# print(*nums)
#
# print([1, 2, 3])
# print(1, 2, 3)

def my_func(a, *abcdr):
    print(a)
    print(abcdr)
    # for el in args:
    #     print(el)


# my_func()
my_func(1)
my_func(1, 2)
my_func(1, 2, 3)


