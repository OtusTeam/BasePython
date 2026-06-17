names1 = {'Bob', 'Alice', 'Mary', 'Ivan',}
names2 = {'Mary',  'Tom', 'John', 'anna', 'Vlad', 'Ivan', 'Mila'}

new_names = names1 | names2
new_names = names1.union(names2)

print(new_names)

new_names = names1 & names2
new_names = names1.intersection(names2)
print(new_names)

new_names = names1 - names2
new_names = names1.difference(names2)
print(new_names)

new_names = names1 ^ names2
new_names = names1.symmetric_difference(names2)
print(new_names)

