import time
from functools import lru_cache


@lru_cache(maxsize=None)
def slow_function(n):
    time.sleep(3)
    return n + 100

start_time = time.time()
print(slow_function(10))
print(f'Время затраченное на выполнение функции = {time.time() - start_time:.2f} секунд')


start_time = time.time()
print(slow_function(10))
print(f'Время затраченное на выполнение функции = {time.time() - start_time:.2f} секунд')

start_time = time.time()
print(slow_function(11))
print(f'Время затраченное на выполнение функции = {time.time() - start_time:.2f} секунд')
