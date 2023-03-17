def say_hello():
    # global user
    user = 'Boris'  # local
    print(f'hello, {user}')  # global
    user = 'Boris'  # local


user = 'Ivan'
print(user)
say_hello()
print(user)
