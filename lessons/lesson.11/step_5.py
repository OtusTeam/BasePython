from itertools import cycle


# abc_inf = cycle('ABC')
abc_inf = cycle(['A', 'B', 'C'])

for _ in range(10):
    print(next(abc_inf))
