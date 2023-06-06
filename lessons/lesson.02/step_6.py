users = ['a.ivanov', 'o.petrova', 'a.sergeev']  # users.pop(0)
msg = 'update your profile'

# messages = []
# for el in users:
#     if el.startswith('a'):
#         messages.append(f'{el}, {msg}')

messages = [f'{el}, {msg}'
            for el in users
            if el.startswith('a')]

print(messages)
