
# def pow_numbers(numbers):
#     for number in numbers:
#         print('number = ', number)
#         yield number ** 10
#
#
# generator = pow_numbers(range(1, 3))
# for gen_num in generator:
#     print('number in power: ', gen_num)
#     if gen_num >= 1000000:
#         break
#
# for i in (num ** 7 for num in range(0, 100)):
#     print('i=', i)
#     if i > 10000:
#         break

# next(generator)
# next(generator)
# next(generator)
# next(generator)

# Есть список букв, из каждой буквы нужно сгенерировать слово длиной 3 и вернуть
# ффф ааа ввв

for i in (character*3 for character in ['a', 'b', 'c']):
    print(i)

# Есть список чисел, нужно сгенерировать последовательность Math.pow(x, 4)
for i in (num**4 for num in range(0, 10)):
    print(i)
