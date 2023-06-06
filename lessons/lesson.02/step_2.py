users = ['a.ivanov', 'o.petrova', 's.sergeev']  # users.pop(0)
msg = 'update your profile'
# DRY

for i in range(len(users)):  # [0, 3)
    # print(i)
    print(users[i] + ', ' + msg)

