import re


my_pattern = r'\d+'
my_str = "Мой номер: 123-456-789. Код 9876"

# result = re.findall(my_pattern, my_str)
# print(result)

result = re.search(pattern=my_pattern, string=my_str)
# print(result)
if result:
    print(result.group())


