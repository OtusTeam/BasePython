def sum_to_n(n):
    result = 0
    for i in range(1, n + 1):
        result += i
    return result


def sum_to_n_opt(n):
    return n * (n + 1) // 2


print(sum_to_n(100))
print(sum_to_n_opt(100))
