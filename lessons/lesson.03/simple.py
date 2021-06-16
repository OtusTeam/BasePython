def outer_func(func):
    print('outer_func start')

    def inner_func(*args, **kwargs):
        print('inner start ')
        print('args: ', args, "  kwargs: ", kwargs)
        result = func(*args, **kwargs)
        print('inner end')
        return result

    print('outer_func end')
    return inner_func


@outer_func
def demo_func():
    print('Demo func start')
    print('Demo func end')

# sample_function = outer_func(demo_func)
# sample_function()

# outer_func(demo_func)()


demo_func()
