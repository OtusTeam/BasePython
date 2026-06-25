def decorator(func):
    def wrapper():
        print('До вызова функции')
        func()
        print('После вызова функции')
    return wrapper


# def hello():
#     print('hello world')
#

# hello()

# res = decorator(hello)
# print(res)
# print(type(res))
# res()


@decorator
def hello():
    print('hello world')


hello()
hello()

