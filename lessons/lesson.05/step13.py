names1 = ['Bob', 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'Ivan', 'John', 'anna', 'Ivan', 'Vlad', 'Mila']
names = {'Bob', 'Alice', 'Bob', 'Mary', 'Ivan', 'Tom', 'John', 'anna', 'Vlad', 'Mila'}
names_1 = set(names1)
names_2 = set()

print(names)
print(type(names))
print(names_1)
print(type(names_1))
print(names_2)
print(type(names_2))

new_list = list(names_1)
print(new_list)
print(type(new_list))