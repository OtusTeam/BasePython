def sum_numbers(*numbers):
    # return sum(numbers)
    # print(numbers)
    total = 0
    for number in numbers:
        total += number
    return total


print(sum_numbers())
print(sum_numbers(1))
print(sum_numbers(2, 3))
print(sum_numbers(5, 6, 7, 8))
print(sum_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# odds = [1, 3, 5,]
odds = list(range(1, 14, 2))
print(odds)
print(sum_numbers(*odds))
