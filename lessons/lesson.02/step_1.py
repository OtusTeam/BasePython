users = ['Ivan', 'Olga', 'Nikolay', 'Igor', 'Ivan']  # -> set

# print(set(users))

# i = 0
# while i < len(users):
#     # print(users[i])
#     # print(f'{i + 1}: {users[i]}')
#     print(i + 1, users[i])
#     i += 1

# i = 0
# for el in users:
#     i += 1
#     print(i, el)

# for i, el in enumerate(users):
#     print(i + 1, el)


# # for i, el in enumerate(users, start=1):
for i, el in enumerate(users, 1):
    print(i, el)

# for el in enumerate(users, 1):
#     i, el = el
#     # print(el)
#     print(i, el)
