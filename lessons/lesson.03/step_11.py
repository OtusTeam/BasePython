def nums_1(n=100):  # O(n) memory
    result = []
    for num in range(n):
        result.append(num)
    return result


def nums_2(n=100):  # O(1) memory
    for num in range(n):
        yield num  # pause


my_nums = nums_1(10)
my_sum = sum(my_nums)
print(my_sum)
print(type(my_nums))
print(my_nums[:5])

print('=' * 80)
my_nums_2 = nums_2(10)
my_sum = sum(my_nums_2)
print(my_sum)
print(type(my_nums_2))
