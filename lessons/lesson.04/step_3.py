import time



def profile(func):
    def inner(a, b):
        start = time.monotonic()

        result = func(a, b)

        finish = time.monotonic()
        print(f'{func.__name__}: {finish - start} sec')

        return result

    return inner


@profile
def sum_sqr(a, b):
    return a ** 2 + b ** 2


# fake_callback = profile(sum_sqr)
# # fake_callback = inner(2, 3)
# # print(fake_callback.__name__)
# result = fake_callback(2, 3)
# print(result)

# # callback
print(sum_sqr(2, 3))
# print(sum_sqr(1, 2))
# print(sum_sqr(3, 4))
# # print(inner(2, 3))
