users = ['a.ivanov', 'o.petrova', 's.sergeev']  # users.pop(0)
msg = '''update your profile'''

# messages = []
# for el in users:
#     messages.append(f'{el}, {msg}')
messages = [f'{el}, {msg}' for el in users]  # list compr...

print(messages)

# for message in messages:
#     print(message)
