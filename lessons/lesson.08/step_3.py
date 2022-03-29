from collections import namedtuple

User = namedtuple('User', 'pk, name, age')
AdminUser = namedtuple('AdminUser', 'pk, name, age')

user_1 = User(1, 'Ivan', 25)
# user_2 = User(1, 'Ivan', 25)
user_2 = AdminUser(1, 'Ivan', age=25)
print(user_1)
print([user_1, user_2])
print(user_1.name)
print(id(user_1), id(user_2))
print(user_1 == user_2)
print(tuple(user_1))
print(user_1[0])
print(User.mro())
# user_1.name = 'Boris'
# print(user_1)
