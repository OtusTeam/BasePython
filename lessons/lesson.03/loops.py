# Распечатать числа от 1 до 10
# Списки и while
# Посчитать сумму чисел в списке
# Цикл в одну строку - while/for - Single-line Loop
# Ключевые слова break, continue, else, pass

# for i in range(1, 11):
#     print(i)

# i = 1
# while i < 11:
#     print(i)
#     i += 1

# numbers = [1, 2, 3, 4]
# # len(numbers) != 0
# while numbers:
#     print(numbers.pop())
# print(numbers)

# numbers = [1, 2, 3, 4]
# i = 0
# while i < len(numbers):
#     print(numbers[i])
#     i += 1
# print(numbers)

# Найти элемент в данном списке
# numbers = [1, 2, 3, 4]
# i = 0
# searched_number = 5
# while i < len(numbers):
#     if numbers[i] == searched_number:
#         print('Number is found')
#         print('Число найдено')
#         break
#     i += 1

# for i in range(0, 5): print(i); print(i)
# counter = 0
# while counter < 5: counter += 1; print(counter); print(counter)

# Continue
# i = 0
# sample_list = [1, 2, 'e',  3, 4]
#
# while i < len(sample_list):
#     if sample_list[i] == 'e':
#         print('*')
#         i += 1
#         continue
#     print(sample_list[i])
#     i += 1

# Else
# i = 0
# while i < 10:
#     i += 1
#     print(i)
# else:
#     print("Else is executed.")

# Pass

# sample_list = [1, 2, 3, 4]
# i = 0
#
# while i < len(sample_list):
#     i += 1
#     pass

# for i in range(0, 5):
#     if i == 3:
#         continue
#     for j in range(0, 2):
#         if j == 1:
#             continue


# Блок инструкций внутри else
# выполнится только в том случае, если выход из цикла произошел без помощи break.
index = 0
while index < 10:
    if index % 2 == 0:
        break
    index += 1
else:
    print('else executed.')
