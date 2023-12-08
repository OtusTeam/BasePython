def profile_it(func):
    print(func)

    def inner(*args, **kwargs):
        print(args)
        print(kwargs)

        result = func(*args, **kwargs)

        print(result)

        return result

    return inner


@profile_it
def sum_squares(*args):
    return sum(el ** 2 for el in args)


# result = sum_squares(2, 3)
# result = profile_it(sum_squares)(2, 3)
# result = inner(2, 3)

print(sum_squares(2, 3))
print(sum_squares(2, 3, 5))
