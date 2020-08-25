from itertools import combinations, combinations_with_replacement, count

nums = list(range(10))

print(nums)
print(list(combinations(nums, 3)))


print(list(combinations_with_replacement(nums, 3)))

odds = count(start=1, step=2)
print(list(next(odds) for _ in range(10)))
