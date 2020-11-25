"""
Our first program
"""

# print("Hello world!")

MAX_RETRIES = 100_000


hello_string = 'Hello world!'

print(hello_string)

multiline_str = '''Hello,
look at these double quotes: """
and quotes: ''
and three of them: \'''
'''

print(multiline_str)

print(repr(hello_string))
print(type(hello_string))
hello_string = 1
print(repr(hello_string))
print(type(hello_string))

hello_string = "Hi!"

print(1 + 1)
print("1" + "1")
print("spam " + "eggs")
print("spam" + "eggs")

print(2 ** 64)
print((2 ** 64) ** 2)
print(2 ** (64 ** 2))
print(2.00001 ** 300)


print("")


print(-1)
print(-10_000_000_000_000_000_000_000)
print(-10000000000000000000000)
print(10000000000000000000000)

print(3)
print(3.0)
print("3 == 3.0", 3 == 3.0)
print("3 == 3.000000000001", 3 == 3.000000000001)
print(3.5)
float_value = 3.5
print(float_value.as_integer_ratio())
print(7 / 2)
print(7 / 1)

print(7 // 2)
print(7 // 1)

print("7 % 2 =", 7 % 2)

print(100 // 17)
print(100 % 17)


print(1/3)
print(2/3)

res = 2 / 3
res_string = "2 / 3 = {:.35f}".format(res)
print(res_string)
print(res - res)
print(2 / 3 - 1 / 3)

# money:
# - only cents 100 + 200 (3$)
# - Decimal
# - separate main, cents 1.5$ + 2.7$ == (1 + 2), (50 + 70) = 4.2$
print(1.5 + 2.7)

a = 4
b = 4

if a > b:
    print("a is greater than b")
elif a == b:
    print("a eq b")
else:
    # print("a is not greater than b")
    print("a is less than b")


# строчка_привет = "привет мир"
# печать = print
# печать(строчка_привет)


some_string = "abcdefg"
for c in some_string:
    print(c, end=" ")
print()

my_list = ['a', 42, True, "abc", ["qwe", "foo", "bar"]]

print(my_list)


for i in my_list:
    print(i, end=" ")

print()

# index = 0

for index, elem in enumerate(my_list):
    print(index, elem)
    # index += 1

    # index = index + 1
    # index -= 1
    # index /= 2
    # index += 1

    # print("in")
# print("out")

my_tuple = ()
print(my_tuple)
# print(repr(my_tuple))
my_tuple = (1., 2, True, False, "str", ["qwe"])
print(my_tuple)

my_list = [1, 2, 3]
print(my_list)
my_list.append(4)
print(my_list)

another_list = my_list

another_list.append(5)
print(another_list)
print(my_list)
print("another_list == my_list", another_list == my_list)
print("another_list is my_list", another_list is my_list)
a = 3
b = a
a = 4
b = 5
print(a, b)

another_list = my_list[:]
print("another_list == my_list", another_list == my_list)
print("another_list is my_list", another_list is my_list)
print(another_list)
print(my_list)
another_list.append(6)
print(another_list)
print(my_list)

# l = list()
# l = []

my_list = [1, 2, 3]
my_tuple = tuple(my_list)
print(my_list)
print(my_tuple)

my_list.append(4)
print(my_list)
print(my_tuple)

print(my_list[0], my_list[3])
print(my_tuple[0], my_tuple[2])

my_t = (7, 9)
(a, b) = my_t
print(a)
print(b)

# my_t = 1,2,3
my_t = (1,2,3)
a,b,c = my_t
print(a,b,c)

strings = ("foo", "bar", "baz")

for s in strings:
    print(s)


for s in enumerate(strings):
    print(s)

for (i, s) in enumerate(strings):
    print(i, s)


for i, s in enumerate(strings):
    print(i, s)

hello_string = "Hello!"
print(hello_string[0], hello_string[5])
print(hello_string[-1])
print(hello_string[-3])

#  H  E  L  L  O
#  0  1  2  3  4
# -5 -4 -3 -2 -1

h = "HELLO"
print(h[0])
print(h[-5])


#    H   E   L   L   O
#  0   1   2   3   4   5
print(h[1:3])
print(h[0:5])
print(h[:])
print(h[1:])


my_set = {4, 1, 2, 3}
print(my_set)
my_list = [1, 2, 3, 4]
print(my_list)
my_list.append(1)
my_list.append(3)
print(my_list)

my_set.add(3)
my_set.add(5)
print(my_set)
my_set.add("qwe")
my_set.add(("foo", "bar"))
print(my_set)

# err
# my_set.add([])

some_list = [1, 2, 2, 3, 4, 4, 5, 6, 6 ,6, 6, 6]
print(some_list)
some_list = list(set(some_list))
print(some_list)

print("6 in some_list", 6 in some_list)
print("9 in some_list", 9 in some_list)

print("4 in my_set", 4 in my_set)
print("7 in my_set", 7 in my_set)


my_dict = {"foo": "bar"}
print(my_dict)

my_dict["spam"] = "eggs"
print(my_dict)
d = my_dict
d["foo"] = "baz"
print(my_dict)

if "foo" in my_dict:
    print("my dict contains", repr(my_dict["foo"]), "by 'foo'")

for num in my_set:
    print(num)

for key in my_dict:
    print(key, my_dict[key])


for key, value in my_dict.items():
    print(key, value)

print(my_dict.values())
print(list(my_dict.values()))
