def make_messages(users, msg='update your profile'):
    messages = []
    for el in users:
        messages.append(f'{el}, {msg}')
    return messages


def send_messages(messages):
    for message in messages:
        print(message)


users = ['a.ivanov', 'o.petrova', 's.sergeev']
msgs = make_messages(users)
send_messages(msgs)

users_2 = ['a.sidorov', 'i.dmitrieva']
msgs_2 = make_messages(users_2, 'delete your profile')
send_messages(msgs_2)
