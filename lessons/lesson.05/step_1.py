def say_hello():
    global user
    print(f'hello, {user}')
    user = 'Boris'


user = 'Ivan'
print(user)
say_hello()
print(user)
