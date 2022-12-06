users = ['Ivan', 'Olga', 'Nikolay', 'Igor', 'Ivan']

users_logins = []
for user in users:
    users_logins.append(user.lower())
print(users_logins)

# users_logins_2 = map(str.lower, users)
# users_logins_2 = map(lambda user: f'@{user.lower()}', users)
# users_logins_2 = map(len, users)
# users_logins_2 = [len(user) for user in users]
users_logins_2 = [user.lower() for user in users]  # list comprehension
print(users_logins_2)
# print(list(users_logins_2))
# print(*users_logins_2)
# print(len('Ivan'))
