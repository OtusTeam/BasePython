def add_nums(num1, num2=10, num3=100):
    # print(f'{num1} + {num2} + {num3} = {num1 + num2 + num3}')
    result = num1 + num2 + num3
    return result
    # return None


res_1 = add_nums(111)
print(res_1)

x = 1200
res_2 = add_nums(num3=x, num1=30)
print(res_2)

