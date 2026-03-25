def add_nums(num1, num2=10, num3=100):
    # print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')
    result_1 = num1 + num2 + num3
    result_2 = num3 - num2 - num1

    return [result_1, result_2]
    # return None


res_1, res_2 = add_nums(1)
# print(res_1, res_2)
my_list = add_nums(1)
print(my_list)
# print(type(res_1))

# x = 1200
# res_2 = add_nums(num3=x, num1=30)
# print(res_2)

