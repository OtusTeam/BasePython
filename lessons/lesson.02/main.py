x = 3
y = 3
age = 30
if 0 < age < 10:
    print('1')
elif age < 20:
    print('2')
elif age < 30:
    print('3')
elif age < 40:
    print('4')
    if x == 3:
        print('x=3')
    else:
        print('x!=3')

else:
    print('NO')

print('END')


######################################

x = 0
count = 5
while count < 0:
    x = x + 3

    count -= 1
    if count == 3:
        break
    print(f'{count} - {x}')
else:
    print(1111)

print(f'Итоговое значение {x}')


#####################################


my_list = [1, 7, 3, 4, 5, 121, "trgb", True ]
for item in my_list:
    print(item)
    item = 111
print(my_list)


######################################


nums = range(10, -2, -1)
print(*nums)


####################################


my_list = [1, 7, 3, 4, 5, 121, "trgb", True ]
for i in range(len(my_list)):
    print(f'{i} - {my_list[i]}')
    my_list[i] = 111

print(my_list)


###################################


my_list = [1, 7, 3, 4, 5, 121, "trgb", True ]
for item in enumerate(my_list, start = 1120):
    #print(f'{i} - {my_list[i-1]}')
    # my_list[i] = 111
    print(item)

print(my_list)


####################################


print('Привет, Боб')
print('Привет, Боб')
print('Привет, Боб')


def greet1():
    print('Привет, Ann')


print(greet1())
greet1()
greet1()
greet1()
greet1()


def greet2(name1: str, name2) -> None:
    print(f'Привет, {name1} {name2}')

greet2('Bob', 'Bob2')
greet2('Ann', 'Bob3')
greet2('John', 'Bob4')



def greet3(num1, num2):
    if num1 > num2:
        result = num1 + num2
        return list[result, num1, num2]
    else:
        result = num2 - num1
    return result

print(greet3(22, 12))



NUMBER = 7
def greet4(num1, num2=NUMBER):
    if num1 > num2:
        result = num1 + num2
        return list[result, num1, num2]
    else:
        result = num2 - num1
    return result

print(greet4(22))



def greet5(num1, num2):
    if num1 > num2:
        result = num1 + num2
        return list[result, num1, num2]
    else:
        result = num2 - num1
    return result

print(greet5(num2=22, num1=17))



def greet6(num1, *args):
    print(num1)
    return args

print(*greet6(1, 2, 3, 4, 5, 7))



def greet7(*args, **kwargs):
    print(args)
    return kwargs

print(greet7({'num1':1}, num2=3, num5=7))



my_list1 = ['1', '2', '3']
res = list(map(int, my_list1))
print(res)


my_list2 = [10, 7, 15]
res = filter(lambda x: x > 9, my_list2)
print(res)


my_list2 = [10, 7, 15]
res = list(filter(lambda x: x > 9, my_list2))
print(res)


def my_func(x):
    return x > 9

my_list3 = [10, 7, 15]
res = list(filter(my_func, my_list3))
print(res)
