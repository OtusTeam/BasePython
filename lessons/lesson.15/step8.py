import re


my_pattern = 'cat'
# string = 'The cat and dog'
# string = 'The dog and dog'
string = 'The cat and  cat dog cat'

# result = re.match(my_pattern, string)
# if result:
#     print(result.group())


# result = re.search(my_pattern, string)
# # if result:
# print(result)


result = re.findall(my_pattern, string)
# if result:
print(result)