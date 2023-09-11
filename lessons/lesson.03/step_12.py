def nums_2(n=100):  # O(1) memory
    for num in range(n):
        yield num  # pause


print('=' * 80)
my_nums_2 = nums_2(10)

print(next(my_nums_2))  # 0
print(next(my_nums_2))  # 1

my_sum = sum(my_nums_2)  # 2
my_sum_3 = sum(my_nums_2)
print(my_sum, my_sum_3)
