import itertools
from itertools import cycle, chain
from timeit import repeat

# counter = itertools.count(start=5, step=3)
#
# for _ in range( 105):
#     print(next(counter))


my_colors = ['red', 'green', 'blue']

cycler = itertools.cycle(my_colors)
for _ in range(25):
    print(next(cycler))


repeat = itertools.repeat('Hello world', 5)
for item in repeat:
    print(item)

for item in repeat:
    print(item)


list_1 = [1, 2, 3]
list_2 = [4, 5, 6]
list_3 = [7, 8, 9]

chained = itertools.chain(list_1, list_2, list_3)
for item in chained:
    print(item)

for item in chained:
    print(item)