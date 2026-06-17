name_1 = 'Bob'
name_2 = 'Alice'
name_3 = 'Mary'
name_4 = 'Ivan'
name_5 = 'Tom'
name_6 = 'John'


names = [name_1, name_2, name_3, name_4, name_5, name_6, 'Anna']
print(names)
print(id(names))
print(type(names))

names.append('Vlad')
print(names)
print(id(names))
print(type(names))

names.append('Mila')
print(names)