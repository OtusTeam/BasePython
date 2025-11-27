import re


my_pattern = r'\d+'
string = 'Мой номер телефона 123-456-789. Код 0022'


result = re.findall(my_pattern, string)
print(result)