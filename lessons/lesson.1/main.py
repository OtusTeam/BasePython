import sys

print('Hello world!')

print(1 + 2)
print(3 - 1)
print(3 * 5)
print('max 32 bit', 2 ** 32)
print('max 64 bit', 2 ** 64)
print('max 64 bit from', -2 ** 64 // 2, 'to', 2 ** 64 // 2)
print('python overload', 2 ** 64 * 2 ** 64)
print('size of 0:', sys.getsizeof(0), 'bytes')
print('size of 2^64:', sys.getsizeof(2 ** 64), 'bytes')
print('foo', 'bar', 'spam', 'eggs')
print('spam' + 'eggs')
print('spam' + ' and ' + 'eggs')
print(10 / 5)
print(11 / 2)
print(10 // 5)
print(11 // 2)
print(11 % 2)
print(15 % 4)
print(1.0 + 2)
print(.0 + 1)
print(.5 + 1.5)
print(1 + 1.5)
print('foo' * 3)
print('a' * 7 + 'b' * 3)

CONSTANT_PI = 3.1415
print('constant pi:', CONSTANT_PI)
print(True, False)
print(True + False, False + False, True + True)
print(True is True, True is False, False is False)

l_from_list = list()
print(l_from_list)
l = []
print(l)
print(l_from_list == l)
print((l_from_list == l) is True)

a = 1
b = a
b = 2
print('a', a, 'b', b)

l1 = [1, 2, 3]
l2 = l1
l3 = l1
l2 = [4, 5, 6]
l4 = [1, 2, 3]

print('l1', l1, 'l2', l2, 'l3', l3, 'l4', l4)
l1[0] = 6
l3[2] = 7
print('l1', l1, 'l2', l2, 'l3', l3, 'l4', l4)
print('l1 is l3:', l1 is l3)
print('l1 is l4:', l1 is l4)
print('l1 is l2:', l1 is l2)
print('len of l1:', len(l1))
print('last array l2 elem:', l2[len(l2) - 1])
print('last array l2 elem:', l2[-1])
print('pre last array l2 elem:', l2[-2])


#  | 6 | 7 | 8 | 9 |
#  0   1   2   3
# -4  -3  -2  -1

array = [1, 2, 3, 4, 5, 6, 7]
print('array[1:3]', array[1:3])
print('array[0:3]', array[0:3])
print('array[:3]', array[:3])
print('array[:]', array[:])

array_copy = array[:]
array_copy.append(8)
array_copy_list = list(array_copy)
array_copy_list.append(9)
array_copy_list_copy = array_copy_list.copy()
array_copy_list_copy.append(0)
print(array, array_copy, array_copy_list, array_copy_list_copy)
print(list('abcdef'))

#

num = 5

if (num % 2 == 0):
    print('num is even')
else:
    print('num is odd')

res = 2 - 3

if res > 0:
    print('greater than zero')
elif res < 0:
    print('smaller than zero')
else:
    print('is zero')

for i in 'abcdef':
    print(i)

line = 'spam eggs foo bar baz'
print('words in line:', line.split())
print('separate:')
for word in line.split():
    print(word)

print('empty list:', bool([]))
print('not empty list:', bool([0]))

array_of_words = line.split()

while array_of_words:
    word = array_of_words.pop()
    print('removed', word)
    print('remains', array_of_words)


array_of_arrays = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(array_of_arrays)
for arr in array_of_arrays:
    print(arr)
#

d = {
    1: 'A',
    2: 'B',
    3: 'C',
}
d2 = d
d[4] = 'D'
print(d)
print(d[1])
print(d2[4])
d2['foo'] = 'bar'
print(d2)
print('pop foo', d2.pop('foo'))
print(d2)

for k in d:
    print(k, '=', d[k])

for k, v in d.items():
    print(k, '=', v)

s = {1, 2, 3, 1, 2, 3, 3}
s.add(4)
print(s)

for i in s:
    print(i)

# t = tuple()
t = (1, 2, 3)
print(t)
dct = {
    (1, 2, 3): [4, 5, 6],
    (7, 8, 9): [0],
}

print(dct)
print(dct[(7, 8, 9)])

t1 = (1, 2, 3)
t2 = t1
print(t1 is t2)

country_codes = {'RU', 'US', 'FR'}
print('ES?', 'ES' in country_codes)
print('RU?', 'RU' in country_codes)

country_codes_main = {'RU', 'US', 'FR'}
country_codes_secondary = {'ES', 'GE', 'RU'}
print(country_codes_main.difference(country_codes_secondary))
print(country_codes_main - country_codes_secondary)
print(country_codes_secondary - country_codes_main)
print(country_codes_main.intersection(country_codes_secondary))
print(country_codes_main & country_codes_secondary)


for i in [2, 11, 13, 4, 6, 7, 8, 9]:
    if i > 10:
        continue
    print(i)
    if i % 2 != 0:
        break

for i in [2, 4, 6]:
    if i % 2 != 0:
        break
    print(i)
else:
    print('did not break')

for i in [1]:
    print('gonna break')
    break
else:
    print('never shows')
