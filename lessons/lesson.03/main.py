# temp = 25
# day = False
#
# print('До блока if')
#
# if temp > 20 or day:
#     print('На улице жарко и солнце')
# elif temp > 10 or day:
#     print('На улице тепло')
# elif temp > 0 or day:
#     print('На улице прохлодно')
# else:
#     print('На улице мороз')
#
# print('После блока if')

# number = '123т'
# if number.isdigit() and int(number) > 100:
#     print('Число больше ста')
#
# command = input("Введите команду: ")
# if command in ("1", "arm"):
#     print("Первое условие")
# elif command in ("2", "disarm"):
#     print("Второе условие")

# a = 5
# # number = None
# if a > 10:
#     number = 10
# else:
#     number = None
# number = 10 if a > 10 else None
# print(number)

# string = 'YN'
# a = -5
# print(string[0 if a > 0 else 1])

# number = 20
# if number > 0:
#     if number >= 10:
#         # print('Число больше либо равно 10')
#         if number > 100:
#             print('Больше ста')
#         else:
#             print('Число меньше ста')
#     else:
#         print('Число положительное, но меньше 10')
# else:
#     print('Число меньше ноля или ноль')

# a = 1
# print(a)
# a += 1
# print(a)
# a +=1
# print(a)
# a = 10
# while a > 0:
#     print(a)
#     a -= 3

# while True:
#     data = input('Введите данные: ')
#     if data == 'exit':
#         break
#     print(data)

# data = input('Введите данные: ')
# while data != 'exit':
#     print(data)
#     data = input('Введите данные: ')
# data = 'ASDFGHYTEL:JRKJBCWLKJCOC"|E:"V<EL'
# user_data = input('Введите символ для поиска: ')
# i = 0
# while i < len(data):
#     if data[i] == user_data:
#         print(data[i])
#         break
#     i += 1
# else:
#     print(f'Символ {user_data} в строке не найден')


# while True:
#     data = input('Введите число: ')
#     if data == 'exit':
#         break
#     if not data.isdigit():
#         continue
#     print(int(data))

# while True:
#     data = input('Введите число: ')
#     if data == 'exit':
#         break
#     if data.isdigit():
#         print(int(data))

string = 'ASDFG'
# i = 0
# while i < len(string):
#     print(string[i])
#     i += 1


# for i in range(len(string)):
#     if string[i] == 'Й':
#         print(f'Нашел {i}')
#         break
# else:
#     print('Буква не найдена')

def lovefunc(flower1, flower2):
    if flower1%2 and not flower2%2 or not flower1%2 and flower2%2:
        return True
    else:
        return False

