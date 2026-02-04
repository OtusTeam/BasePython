import re


my_pattern = r"cat"
# my_str = "123 cat and cat dog"
my_str = "123 cot and cit dog"

# result = re.match(pattern=my_pattern, string=my_str)
# print(result)
#
# if result:
#     print(result.group())
#

# result = re.search(pattern=my_pattern, string=my_str)
# print(result)
#
# if result:
#     print(result.group())

#
result = re.findall(pattern=my_pattern, string=my_str)
print(result)

