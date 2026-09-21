def dec(func):
    def wrapper(*args, **kwargs):
        print('До вызова функции')
        func()
        print('После вызова функции')
    return wrapper


def hello():
    print("Привет!")


my_hello = dec(hello)
print(my_hello)
my_hello()