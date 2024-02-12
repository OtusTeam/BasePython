"""
f(n) = n * (n-1) * (n-2) * ... * 1
f(n) = n * f(n-1)
"""


def factorial_cycle(n):
    """
    f(n) = n * (n-1) * (n-2) * ... * 1

    :param n:
    :return:
    """
    result = 1
    # for num in range(1, n + 1):
    for num in range(n, 1, -1):
        result *= num
    return result


def factorial(n):
    """
    f(n) = n * f(n-1)

    :param n:
    :return:
    """
    if n < 3:
        return n
    res = n * factorial(n - 1)
    return res


print(factorial_cycle(4))
print(factorial_cycle(5))
print(factorial_cycle(6))
print(factorial_cycle(10))
# print(factorial_cycle(1001))
print()
for i in range(1, 11):
    print(i, factorial(i))

print(factorial(100))
# print(factorial(1001))
