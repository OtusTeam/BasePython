# def calc_nums(num_1, num_2, num_3):
#     result_add = num_1 + num_2 + num_3
#     return result_add
#
#
#
# res_1 = calc_nums(1, 2, 3, 4, 5, 6, 7)
# print(res_1)

# def calc_nums(*nums):
#     print(nums)
#     print(type(nums))
#
#
# # res_1 = calc_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# res_1 = calc_nums()
# # print(res_1)


def calc_nums(num_1, num_2, *args):
    print(args)
    print(num_1)
    print(num_2)
    print(type(args))


res_1 = calc_nums(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
# res_1 = calc_nums()
# print(res_1)