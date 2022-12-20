def args_logger(func):
    # cache = {}
    def inner(*args, **kwargs):
        # nonlocal cache
        result = func(*args, **kwargs)
        print(f'args {args}, kwargs {kwargs} -> {result}')
        return result

    return inner


@args_logger
def prod(x, y):
    return x * y


print(prod(5, 7))
