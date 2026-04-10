from my_friends.add_friend import add_f
from my_friends.remove_friend import del_f, del_i


friends = ['Боб', 'Анна', 'Иван']
name = 'Мэри'
print(add_f(friends, name))
print(friends)

name = 'Иван'
print(del_f(friends, name))
print(friends)

i = 0
print(del_i(friends, i))
print(friends)