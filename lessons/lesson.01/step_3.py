users = ['Ivan', 'Bob', 'Olga']
print(type(users))
# print(dir(users))
print(users)
print(users[-1])
print(users[len(users) - 1])

users.append(15)
print(users)
last_el = users.pop()
print(last_el)
print(users)
