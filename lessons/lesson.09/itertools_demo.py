from itertools import chain, combinations, combinations_with_replacement, count, repeat, cycle, zip_longest

results = [
    ['Engineer'],
    ['Manager'],
    ['Support'],
    ['QA'],
]

# print(list(chain(*results)))

nums = range(10)
# print(nums)
# print(list(combinations(nums, 2)))
# print(list(combinations(nums, 3)))
# print(list(combinations_with_replacement(nums, 2)))
#
#
odds = count(start=1, step=2)
# print(list(next(odds) for _ in range(10)))

# r_5 = repeat(5)
# print([next(r_5) for _ in range(7)])
#
#
# c_names = cycle(["John", "Sam", "Nick"])
# print([next(c_names) for _ in range(13)])


a = (1, 2, 3)
b = ("a", "b", "c")
c = ("X", "Y", None)

print(list(zip(a, b, c)))
# result = [(1, 'a', 'X'), (2, 'b', 'Y'), (3, 'c', 'Z')]
# print(list(zip(*result)))
#
k = (1, 2, 3, 3)
j = ("A", "B", 'C')

print(list(zip(k, j)))
print(set(zip_longest(k, j, fillvalue='Z')))

print(zip(k, j))
print(type(zip(k, j)))

#
# my_list = range(17)
#
# # print(list(grouper(my_list, 5)))
