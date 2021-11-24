sample_list = [0, 1, 2, 3, 4, 5, 6]

# Возможность получать каждый из элементов следующим
# print(type(i for i in sample_list))


# Вычислить десятую степень чисел в списке
def power_numbers(numbers):
    for number in numbers:
        yield number ** 10


# generator = power_numbers(sample_list)

# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))
# print(next(generator))


# for num in generator:
#     print(num)

# for num in generator:
#     print(num)
#     if num > 2000000:
#         break

# for num in (number**10 for number in sample_list):
#     print(num)
#     if num > 2000000:
#         break
#
# next(generator)
# next(generator)


for num in [i for i in range(100) if i % 7 == 0]:
    print(num)

