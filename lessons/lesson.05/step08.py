names = ['Bob', 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'Anna', 'Vlad', 'Mila']
print(names)

# name = names.remove('Bob')
# names.remove('Bob')
#
# print(names)
# print(name)

# names.remove('Bob')
# print(names)
#
# for name in names:
#     print(name)
#     if name == 'Bob':
#         names.remove('Bob')
#
# print(names)


while 'Bob' in names:
    names.remove('Bob')

print(names)

# num = names.count('Tom')
# print(num)
#
# index = names.index('Bob')
# print(index)