import re


my_pattern = r'cat'
my_str = "cat123 cat and cit dog"

result = re.match(my_pattern, my_str)
# print(result.group())
if result:
    print(result.group())


