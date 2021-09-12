# Ключевые и позиционные аргументы и результаты


# def sum_numbers(a, b):
#     return a + b

# def sum_numbers(a, b, *args):
#     # print(type(numbers))
#     print(a, b)
#     numbers_sum = 0
#     for number in args:
#         numbers_sum += number
#     return numbers_sum
#
#
# print(sum_numbers(1, 2, 3, 4, 5, 6))

# def print_user_details(test, *args, **kwargs):
#     # print(type(kwargs))
#     print(kwargs)
#     for keyword in kwargs.keys():
#         print(keyword)
#
#     print(kwargs.items())
#     for keyword, detail in kwargs.items():
#         print(keyword, ' = ', detail)
#
#     for detail in kwargs.values():
#         print(detail)

# def print_user_details(**kwargs):
#     print(kwargs.get('test'))
#     print(kwargs['name'])
#     if 'name' in kwargs.keys():
#         print(kwargs['name'])
# for keyword, detail in kwargs.items():
#     if keyword == 'name':
#         print(detail)


# print_user_details(name='Nigar', surname='Movsumova')

# def my_sum(a, b, c):
#     print(a + b + c)
#
#
# my_list = [1, 2, 3]
# my_sum(*my_list)

#
# def print_dict(name, surname):
#     print(name, surname)
#
#
# my_dict = {"name": "test", "surname": "test"}
# print_dict(**my_dict)

def find_max_min(numbers):
    max = numbers[0]
    min = numbers[0]
    for number in numbers:
        if number > max:
            max = number
        if number < min:
            min = number
    return min, max


numbers = [-4, 1, 2, 3, 4, 5]
list_min, list_max = find_max_min(numbers)
print(list_min, list_max)
