import re


my_pattern = r'\b[\w.-]+@[\w.-]+\.\w+\b'
my_str = "Мой номер: 123-456-789. Код 9876 Или пишите на почту ivan@mail.ru и maria@gmail.com"

result = re.findall(my_pattern, my_str)
print(result)



