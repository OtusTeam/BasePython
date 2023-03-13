# for num in range(5):  # [0, n)
#     print(num)

# DRY
users = ['i.ivanov', 'a.andreeev', 's.sergeev']


# print('hello', 'i.ivanov')
# # print('hello', 'i.ivanov', 'have a good day')
# print('hello', 'a.andreeev')
# print('hello', 's.sergeev')  # 100 000 000


def say_hello(user_name):
    print('hello', user_name, 'have a good day!')


# say_hello('i.ivanov')
# say_hello('a.andreeev')
# say_hello('s.sergeev')
def greet_users(users):
    for user_name in users:
        say_hello(user_name)


greet_users(users)
