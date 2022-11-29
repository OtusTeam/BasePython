users = ['Ivan', 'Bob', 'Olga']
# users = list(('Ivan', 'Bob', 'Olga'))
users_backup = users
print(id(users), id(users_backup))
print(users is users_backup)
print(users == users_backup)

last_user = users.pop()
print(users)
print(users_backup)
