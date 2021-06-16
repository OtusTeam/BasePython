# 1. While

# number = int(input('Enter a number:'))
#
# while number < 10:
#     print(number)
#     number += 1


# 2. Lists

# sample_list = [1, 2, 3, 4]
# while sample_list:
#     print(sample_list.pop())
#
# print(sample_list)
# index = 0
# while index < len(sample_list):
#     print(sample_list[index])
#     index += 1
#
# print(sample_list)

# 3. Break

# sample_list = [1, 2, 3, 4, 6]
#
# i = 0
# while i < len(sample_list):
#     print(sample_list[i])
#     i += 1
#     if sample_list[i] == 3:
#         break

# 4. Single-line While Loop

# count = 0
# while count < 5: count += 1; print("Hello World"); print('test')
#
# for i in range(0, 5): print('t'); print('t')

# 5. Continue
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

# 6. Else
# i = 0
# while i < 10:
#     i += 1
#     print(i)
# else:
#     print("Else is executed.")
#
# i = 0
# while i < 10:
#     i += 1
#     print(i)
#     break
# else:
#     print("Else is executed.")

# Pass


# sample_list = [1, 2, 3, 4]
# i = 0
#
# while i < len(sample_list):
#     i += 1
#     pass
# print('Value of i :', i)

# dict_sample = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
#
# while dict_sample:
#     print(dict_sample.popitem())
#
# print(dict_sample)
# print(dict_sample.popitem())

list = [1, 2, 3]
#
index = 1
# print(type(list.pop(index)) is int)
while list:
    next_num = list.pop(0)
    if type(next_num) == int:
        print('1')
else:
    print('2')

print(list)
