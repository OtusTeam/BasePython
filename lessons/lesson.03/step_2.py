from typing import List


def sum_squares(args: List[float]) -> float:
    # print(args)
    return sum(el ** 2 for el in args)


print(sum_squares([2, 3]))
print(sum_squares([2, 3, 5]))

print([2, 3, 5])
print(*[2, 3, 5])