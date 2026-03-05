name = 'Bob'
my_str = f'{name} Введите значение: '

# user_input = input(my_str)
# user_number = int(user_input)

user_number = int(input(my_str))
print(user_number + 10)
print(type(user_number))

float_number = float(user_number)
print(float_number + 1.1)
print(type(float_number))

user_str = str(float_number)
print(user_str)
print(type(user_str))