name = 'Bob'
age = 10

print(1, 2, 'a', name, age, end='####')
print(1, 2, 'a', name, age, sep='-=-', end='####')
print(1, 2, 'a', name, age)

print('Привет - ', name, 'тебе', age, 'лет')
my_text_1 = f'Привет  - {name} т"ебе {age + 100} лет'
my_text_2 = f"Привет  - {name} т'ебе {age + 200} лет"
my_text_3 = f"""Привет  - '
{name} тебе " {age + 300} 
           лет"""
my_text_4 = f'''Привет
  -     {name} 
     тебе {age + 400} 
  лет'''

print(my_text_1)
print(my_text_2)
print(my_text_3)
print(my_text_4)

ch = 'a'
print(type(ch))