
# def calc_nums(name, age, **kwargs):
#     print(kwargs)
#     print(name)
#     print(age)
#     print(type(kwargs))
#
#
# res_1 = calc_nums(num1=1, num2=2, n3=3, a5=4, age=32, name="Bob")
# # res_1 = calc_nums()
# # print(res_1)


def calc_nums(num_1, num_2, *args, name, age, **kwargs):
    print(args)
    print(type(args))
    print(num_1)
    print(num_2)
    print(kwargs)
    print(name)
    print(age)
    print(type(kwargs))


res_1 = calc_nums(10, 100, 1000, 1111, 2222, n1=1, n2=2, n3=3, a5=4, age=32, name="Bob")
# res_1 = calc_nums()
# print(res_1)