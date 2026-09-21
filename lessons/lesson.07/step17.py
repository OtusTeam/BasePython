def dec(func):
    def wrapper():
        print('До вызова функции')
        func()
        print('После вызова функции')
    return wrapper


@dec
def hello():
    print("Привет!")


hello()