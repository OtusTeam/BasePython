import functools


@functools.lru_cache(3)
def sum_it(a, b):
    """sum two numbers"""
    print(f'calc: {a} + {b}')
    return a + b


print(sum_it(2, 6))
print(sum_it(2, 6))
print(sum_it(6, 2))
# print(sum_it(2, 7))
# print(sum_it(2, 7))
# print(sum_it(2, 8))
# print(sum_it(2, 8))
# print(sum_it(2, 9))
# print(sum_it(2, 9))

# print(sum_it(2, 6))
