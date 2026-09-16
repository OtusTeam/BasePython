def calc_nums(calc, num_1=5, num_2=10, num_3=17):
    if calc == "+":
        result_add = num_1 + num_2 + num_3
        return result_add
        print(111111)
    elif calc == "-":
        result_sub = num_3 - num_2 - num_1
        return result_sub
        print(222222)
    else:
        result = None
        return result
        print(3333333)

    # return None


res_1 = calc_nums("+", 1, 2, 3)
print(res_1)

res_2= calc_nums("-", 1, 2)
print(res_2)

print(calc_nums("+", num_3=100))

res_4= calc_nums("*", num_3=100, num_1=20)
print(res_4)


# age = int(input())