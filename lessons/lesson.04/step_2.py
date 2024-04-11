import time


def profile(func):
    num_calls = 0
    # print('inside profile')
    def inner(a, b):
        # global num_calls
        nonlocal num_calls
        # num_calls = 5
        num_calls += 1

        start = time.monotonic()

        result = func(a, b)

        finish = time.monotonic()
        print(f'{num_calls}: {finish - start} sec')

        return result

    return inner


# @memo_profile
@profile
def sum_sqr(a, b):
    return a ** 2 + b ** 2


# callback
print(sum_sqr(2, 3))
print(sum_sqr(1, 2))
print(sum_sqr(3, 4))
# print(inner(2, 3))
