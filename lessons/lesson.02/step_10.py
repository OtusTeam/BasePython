# from typing import List
#
#
# def make_messages(users: List[str], msg: str) -> List[str]:
def make_messages(users, msg):
    """
    Make list of messages

    :param users:
    :param msg:
    :return: list of messages
    """
    messages = []
    for el in users:
        messages.append(f'{el}, {msg}')
    # print(id(messages))
    return messages


def send_messages(messages):
    for message in messages:
        print(message)
        # return
    # return None


users = ['a.ivanov', 'o.petrova', 's.sergeev']
msg = '''update your profile'''
msgs = make_messages(users, msg)  # call
# print(id(msgs))
print('send_messages', send_messages(msgs))

users_2 = ['a.sidorov', 'i.dmitrieva']
msgs_2 = make_messages(users_2, msg)  # call
send_messages(msgs_2)
