# class IncorrectValueNumber(BaseException):
#     pass


# first = int(input('Enter the first number: '))
# second = int(input('Enter the second number: '))
# print(first + second)

first = None
second = None

# try:
#     first = input('Enter the first number: ')
#     second = input('Enter the first number: ')
#     first = int(first)
#     second = int(second)
#     print(first + second)
# except ValueError:
#     # print(f'Вы ввели неправильное значение для чисел - {first}, {second}')
#     raise BaseException(f'Вы ввели неправильное значение для чисел - {first}, {second}')

# if first is None:
#     print(f'Вы ввели неправильное значение для чисел - {first}')
# else:
#     print(f'Вы ввели неправильное значение для чисел - {second}')

# try:
#     first = input('Enter the first number: ')
#     second = input('Enter the first number: ')
#     first = int(first)
#     second = int(second)
#     print(first / second)
# except ValueError as e:
#     # print(e)
#     raise BaseException(f'Вы ввели неправильное значение для чисел - {first}, {second}')
# except ZeroDivisionError as e:
#     raise Exception(f'На ноль делить нельзя!')
# except (ValueError, ZeroDivisionError) as e:
#     # print(e)
#     raise BaseException(f'Вы ввели неправильное значение для чисел - {first}, {second}')


# try:
#     first = int(input('Enter the first number: '))
# except ValueError:
#     print(f'Вы ввели неправильное значение для чисел - {first}')
#
# try:
#     second = int(input('Enter the first number: '))
# except ValueError:
#     print(f'Вы ввели неправильное значение для чисел - {second}')


# if first < 10:
#     raise IncorrectValueNumber('The number should be > 10.')
# print(first/second)

class NoProductException(BaseException):
    pass

# product_count = int(input('Enter the product count: '))
# if product_count <= 0:
#     raise BaseException('Количество продуктов должно быть больше нуля.')
# elif product_count > 10:
#     raise NoProductException('Нет достаточного количества продуктов!')
# else:
#     print('Перейдите в корзину для покупки!')

# print(15 / 0)


# try:
#     with open('otus', 'r') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)


f = None

# try:
#     f = open('otus')
#     content = f.readlines()
#     print(content)
# except AttributeError:
#     print("file is not found")
# finally:
#     f.close()

# file = open('otus')
# print(file.read())
# file.close()


# class IncorrectValueNumber(BaseException):
#     pass


# try:
#     first = int(input('Enter the first number: '))
#     second = int(input('Enter the second number: '))
#     print(first/second)
# except (ValueError, ZeroDivisionError) as ex:
# print("ex = ", ex)
# raise IncorrectValueNumber(ex)
# except BaseException as ex:
#     print(ex)


# if first < 10:
#     raise IncorrectValueNumber('The number should be > 10.')

#
# try:
#     print(first / second)
# except ZeroDivisionError:
#     raise BaseException('You can not divide by zero.')
#     # print('You can not divide by zero.')


sample_dictionary = {'name': 'Otus', 'site': "otus.ru"}
# try:
#     print(sample_dictionary['sit'])
# except KeyError as ex:
#     # print(ex)
#     raise KeyError(f'\'{ex.args[0]}\' key does not exist in dictionary')

if 'site' in sample_dictionary.keys():
    print(sample_dictionary['site'])
else:
    print(f'\'site\' key does not exist in dictionary')
