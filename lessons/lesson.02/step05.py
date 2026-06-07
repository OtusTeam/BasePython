age: int = 10
print(age)
print(id(age))

age: int = 'bob'
print(age)
print(id(age))


ye = 10.12
print(ye)
print(type(ye))
print(id(ye))

ye += 10
# ye = ye + 10
print(ye)
print(type(ye))
print(id(ye))

name = 'Bob'
print(name)
print(type(name))
print(id(name))

name = name + 'asdfhg'
print(name)
print(type(name))
print(id(name))

my_list = [1, 2, 3]
print(my_list)
print(type(my_list))
print(id(my_list))

my_list.append(4)
print(my_list)
print(type(my_list))
print(id(my_list))

print(type(print))