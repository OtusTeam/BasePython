import copy


names = ['Bob', [1, 2, 3], 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'anna', 'Vlad', 'Mila']
print(names)

# names_1 = names
# names_1 = names[::]
# names_1 = names.copy()
names_1 = copy.deepcopy(names)

print(names_1)

print('*' * 50)


names_1[1].append('kate')
print(names_1)
print(names)
