def add_nums(num_1=5, num_2=10, num_3=17):
    result = num_1 + num_2 + num_3
    return result


res_1 = add_nums(1, 2, 3)
print(res_1)

res_2= add_nums(1, 2)
print(res_2)

res_3= add_nums(num_3=100)
print(res_3)

res_4= add_nums(num_3=100, num_1=20)
print(res_4)