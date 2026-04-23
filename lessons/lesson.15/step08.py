import re


my_pattern = r'cat'
my_str = "123 cat and cit dog"

result = re.search(my_pattern, my_str)
# print(result)
if result:
    print(result.group())


