from itertools import combinations, chain, combinations_with_replacement

results = [
    ['Engineer'],
    ['Manager']
]

print(list(chain(*results)))

nums = range(10)
print(combinations(nums, 2))
print(combinations(nums, 3))
print(combinations_with_replacement(nums, 2))
