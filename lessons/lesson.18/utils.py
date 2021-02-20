from time import perf_counter

from psutil import virtual_memory


def time_prof(func):
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'{perf_counter() - start:.6f}')
        return result

    return wrapper


def show_mem(mem):
    print(f'{(virtual_memory().used - mem) / 2 ** 20:.3f} MB')
