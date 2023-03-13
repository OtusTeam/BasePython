def make_hello(name):
    start = ...
    result = f'{name}, hello!'
    end = ...
    print(f'make_hello: {end - start}')
    return result


def sum_it(*args):
    start = ...
    print(f'sum {len(args)} nums')
    end = ...
    print(f'sum_it: {end - start}')
    return sum(*args)


# func_name: time in sec
