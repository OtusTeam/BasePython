def gen_func():
    for i in range(10):
        yield x * x


gen = (x * x for i in range(10))