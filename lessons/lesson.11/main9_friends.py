# from my_friends import add_f, del_f, del_i
from my_friends import add, d_i, d_f


friends = ['Боб', 'Анна', 'Иван', 'Джон']
name = 'Мэри'
print(add(friends, name))
print(friends)

name = 'Иван'
print(d_f(friends, name))
print(friends)

i = 0
print(d_i(friends, i))
print(friends)