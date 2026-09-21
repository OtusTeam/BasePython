def gen_func():
    x = 10
    yield x
    print(123)
    x += 30
    yield x
    print(345)
    # return 1234567
    x /= 2
    yield x
    print(567)
    x *= 5
    yield x


my_gen = gen_func()
print(my_gen)
print(next(my_gen))
print(next(my_gen))
print(next(my_gen))

