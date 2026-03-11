# age = 29
# name = 'Bob'
#
#
#
# if age < 18:
#
#     print('Школьник')
#     print('Школьник')
# elif age < 25 :
#
#     print('Студент')
# elif age < 50:
#     print('Взрослый')
# else:
#     print('Пенсионер')
#
# print('END')

# or and not
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)
#
# print(1 and 1)
# print(0 and 1)
# print(1 and 0)
# print(0 and 0)
#
# print(5 > 3 and 3 > 7)
# print(5 > 23 and 43 > 7)
# print(5 > 23 and 3 > 27)
# print(5 > 3 and 53 > 7)

# print(True or True)
# print(True or False)
# print(False or True)
# print(False or False)
#
# print(1 or 1)
# print(0 or 1)
# print(1 or 0)
# print(0 or 0)
#
# print(5 > 3 or 3 > 7)
# print(5 > 23 or 43 > 7)
# print(5 > 23 or 3 > 27)
# print(5 > 3 or 53 > 7)

# print(not True)
# print(not False)
#
#
# print(not 1)
# print(not 0)
#
# print(not(5 > 3 or 3 > 7))
# print(not(5 > 23 or 43 > 7))
# print(not(5 > 23 or 3 > 27))
# print(not(5 > 3 or 53 > 7))

# age = 20
# my_bool = age < 18
# print(my_bool)

# if my_bool:
#     pass
# else:
#     print(123)

# if not my_bool:
#     print(123)


age = 19
name = 'Bob'


if age < 18 and name == 'Bob':

    print('Школьник')
    print('Школьник')
elif age < 25 and not (name == 'Bob' or name == 'Ann' ):

    print('Студент')
elif age < 50:
    print('Взрослый')
else:
    print('Пенсионер')

print('END')