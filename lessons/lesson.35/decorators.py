from time import perf_counter


def time_prof(func):
    def wrap(*args, **kwargs):
        started = perf_counter()
        result = func(*args, **kwargs)
        print(f'{perf_counter() - started:.6f}')
        return result
    return wrap
