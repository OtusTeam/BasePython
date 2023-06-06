users = ['a.ivanov', 'o.petrova', 's.sergeev']  # users.pop(0)
msg = '''update your profile'''

# for el in users:
#     print(f'{el}, {msg}')
messages = []
for el in users:
    messages.append(f'{el}, {msg}')

for message in messages:
    print(message)
