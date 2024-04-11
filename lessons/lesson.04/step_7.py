def my_func(a, b=None, c=None, **kwargs):
    print(kwargs)
    print(a, end=' -> ')
    print(b, end=' -> ')
    # print(b, ' -> ')
    print(c)


# my_func(1)
# my_func(1, 2)
# my_func(1, 2, 3)
my_func(1, None, 3)
my_func(1, c=3)  # kwargs
my_func(a=1, c=3)
my_func(c=3, a=1)

kw_1 = {'a': 1, 'c': 3, 'e': 100}
my_func(**kw_1)

instance_1 = ...


def update(**params):
    for k, v in params.items():
        setattr(instance_1, k, v)
