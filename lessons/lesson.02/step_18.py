# def sum_nums(a, b, c=0):
#     return a + b + c
def sum_nums(*args, **kwargs):
    # print(args)
    # print(kwargs)
    return sum(args)


result_1 = sum_nums(3, 7)
print(result_1)

result_2 = sum_nums(3, 7, 4)
print(result_2)

result_3 = sum_nums()
print(result_3)
