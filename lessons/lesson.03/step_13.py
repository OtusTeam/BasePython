def nums_2(n=100):
    return (num for num in range(n))


print('=' * 80)
my_nums_2 = nums_2(10)

print(type(my_nums_2))
print(next(my_nums_2))  # 0
print(next(my_nums_2))  # 1

# my_sum = sum(my_nums_2)  # 2
my_sum = 0
# for el in my_nums_2:
#     my_sum += el

while True:
    try:
        my_sum += next(my_nums_2)
    except StopIteration:
        break

print(my_sum)
# print(next(my_nums_2))
# my_nums_2 = nums_2(10)
# my_sum_3 = sum(my_nums_2)
# print(my_sum, my_sum_3)
