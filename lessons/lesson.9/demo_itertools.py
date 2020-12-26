from itertools import chain, combinations, combinations_with_replacement, count, repeat, cycle, zip_longest

results = [
    ['Engineer'],
    ['Manager'],
    ['Support'],
    ['QA'],
]

print(list(chain(*results)))

nums = range(10)
print(nums)
print(list(combinations(nums, 2)))
print(list(combinations(nums, 3)))
print(list(combinations_with_replacement(nums, 2)))


odds = count(start=1, step=2)
print(list(next(odds) for _ in range(10)))
print(list(nums))

r_5 = repeat(5)

print([next(r_5) for _ in range(7)])


c_names = cycle(["John", "Sam", "Nick"])
print([next(c_names) for _ in range(13)])


def grouper(iterable, n, fillvalue=None):
    """
    Collect data into fixed-length chunks or blocks
    """
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx"
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


a = (1, 2, 3)
b = ("a", "b", "c")
c = ("X", "Y", "Z")

print(list(zip(a, b, c)))
result = [(1, 'a', 'X'), (2, 'b', 'Y'), (3, 'c', 'Z')]
print(list(zip(*result)))

k = (1, 2, 3, 4)
j = ("A", "B")

print(list(zip(k, j)))
print(list(zip_longest(k, j, fillvalue="z")))


my_list = range(17)

print(list(grouper(my_list, 5)))
