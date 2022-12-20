# users = ('Ivan', 'Bob',
#          'Olga')
users = 'Ivan', 'Bob', 'Olga'
# users_backup = users
users_backup = ('Bob', 'Olga')
print(type(users))
print(dir(users))
print(id(users), id(users_backup))
print(users is users_backup)
print(users == users_backup)

# last_user = users.pop()
# print(users)
# print(users_backup)
