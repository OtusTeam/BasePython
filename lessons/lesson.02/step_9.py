def send_messages(users, msg):
    messages = []
    for el in users:
        messages.append(f'{el}, {msg}')

    for message in messages:
        print(message)


print(send_messages)  # callback
# print(dir(send_messages))

users = ['a.ivanov', 'o.petrova', 's.sergeev']
msg = '''update your profile'''
send_messages(users, msg)  # call


users = ['a.sidorov', 'i.dmitrieva']
msg = '''delete your profile'''
send_messages(users, msg)  # call
