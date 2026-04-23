import re


my_pattern = r'cat'
my_str = "cat123 cit and cit cat dog"

result = re.findall(my_pattern, my_str)
print(result)
# if result:
#     print(result.group())


