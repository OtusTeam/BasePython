def log_time(func):
    def wrapper(*args, **kwargs):
        print('started')
        result = func(*args, **kwargs)
        print('finished')
        return result

    return wrapper


@log_time
def make_hello(name):
    return f'{name}, hello!'


@log_time
def sum_it(*args):
    print(f'sum {len(args)} nums')
    return sum(*args)


# func_name: time in sec
# start = ...
# end = ...
# print(f'sum_it: {end - start}')
# result = log_time(make_hello)('Ivan')
print(make_hello('Ivan'))
