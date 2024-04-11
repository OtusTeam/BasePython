import time


# def sum_sqr(a, b):
#     return a ** 2 + b ** 2


def sum_sqr(a, b):
    start = time.monotonic()
    result = a ** 2 + b ** 2
    finish = time.monotonic()
    print(f'{finish - start} sec')

    return result


print(sum_sqr(2, 3))
