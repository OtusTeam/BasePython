def add(a, b):
    return a + b


res1 = add(2, 3)
print("res1", res1)
res2 = add(3.5, 7.5)
print("res2", res2)
res3 = add("foo", "bar")
print("res3", res3)
res4 = add(["foo", "spam"], ["bar", "eggs"])
print("res4", res4)


my_list = [1, 5, 8]
print("my_list:", my_list)
print("id my_list:", id(my_list))
my_list += [0, 7]
print("my_list:", my_list)
print("id my_list:", id(my_list))

new_list = my_list + [1, 2]
print("new_list:", new_list)
print("my_list:", my_list)

a = 3
print("a", a)
print("1 id a", id(a))
b = 6
a = a + b
print("a", a)
print("2 id a", id(a))
a += b
print("a", a)
print("3 id a", id(a))
