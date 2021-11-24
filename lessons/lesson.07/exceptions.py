# class IncorrectValueNumber(BaseException):
#     pass


# first = int(input('Enter the first number: '))
# second = int(input('Enter the second number: '))
# if first < 10:
#     raise IncorrectValueNumber('The number should be > 10.')
# print(first/second)
# import logging


# try:
#     with open('o', 'r') as file:
#         print(file.read())
# except FileNotFoundError as e:
#     print(e)


# f = None

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
#     #     print(ex)
#     raise KeyError(f'\'{ex.args[0]}\' key does not exist in dictionary')

# if 'site' in sample_dictionary.keys():
#     print(sample_dictionary['site'])
# else:
#     print(f'\'site\' key does not exist in dictionary')
