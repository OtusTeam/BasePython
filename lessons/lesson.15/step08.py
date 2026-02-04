import re


my_pattern = r"\d+"
# my_str = "123 cat and cat dog"
my_str = "Мой номер: 123-456-789. Код 9876"

result = re.match(pattern=my_pattern, string=my_str)
print(result)

if result:
    print(result.group())


# result = re.search(pattern=my_pattern, string=my_str)
# print(result)
#
# if result:
#     print(result.group())

#
# result = re.findall(pattern=my_pattern, string=my_str)
# print(result)

