def add_nums(name, *args, age, **kwargs):
    # print(type(kwargs))
    # num_1, *num_2, num_3 = nums
    # print(num_1, num_2, nums)
    print(name)
    print(args)
    print(age)
    kwargs['a'] = True
    return kwargs


my_result = add_nums('Ann', 123, 345, age=19, a=1, b=2, c=3, d=4, e=5)
print(my_result)
print(type(my_result))
