# cnt = 0
# # while True:
# #     # print('hello')
# #     # cnt += 1
# #     if cnt == 3:
# #         break
# #     cnt += 1
# #     print('hello')
#
# while cnt < 3:
#     print('hello')
#     cnt += 1

users = ['i.ivanov', 'a.andreeev', 's.sergeev']
# cnt = 0
# while cnt < len(users):
#     print(users[cnt])
#     cnt += 1  # cnt = cnt + 1

# users = 'hello'
# __method__
to_cont = True
for num in range(5):
    for user in users:
        if user.startswith('a'):
            # to_cont = False
            break
        if user.startswith('s'):
            continue
        print(user)  # next()
    else:
        print('normal termination')
    if not to_cont:
        break
