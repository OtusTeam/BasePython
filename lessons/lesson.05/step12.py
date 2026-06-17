names = ('Bob', [1, 2, 3], 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'anna', 'Vlad', 'Mila')
print(names)
print(type(names))
print(id(names))

print(names[1])
print(names[3])
print(names[1: 5])

print(names[::2])

for name in names:
    print(name)


name_new = list(names)
name_new.append('Bob123')

print(name_new)
print(type(name_new))
print(id(name_new))

names = tuple(name_new)
print(names)


names[1].append(123)
print(names)

names1 = ('Bob', [1, 2, 3], 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'anna', 'Vlad', 'Mila')
names2 = ('Bob', [1, 2, 3], 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'anna', 'Vlad', 'Mila')
print(names1)
print(names2)
print(id(names1))
print(id(names2))

print(names1.count('Bob'))
print(names1.index('Bob'))