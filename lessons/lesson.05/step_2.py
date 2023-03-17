def cache(func):
    results = {}
    def wrapper(*args, **kwargs):
        nonlocal results
        ...
        # results[key] = result


@cache
def sum_it(*args):
    pass


results = {}
sum_it(1, 5)
sum_it(1, 5)
sum_it(1, 5)
sum_it(1, 5)

