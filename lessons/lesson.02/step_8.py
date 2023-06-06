def send_messages(users, msg):
    messages = []
    for el in users:
        messages.append(f'{el}, {msg}')

    for message in messages:
        print(message)


send_messages(['a.ivanov', 'o.petrova', 's.sergeev'],
              'update your profile')

send_messages(['a.sidorov', 'i.dmitrieva'],
              'delete your profile')
