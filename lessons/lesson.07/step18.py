def dec1(func):
    def wrapper():
        print('До вызова функции1')
        func()
        print('После вызова функции1')
    return wrapper


def dec2(func):
    def wrapper():
        print('До вызова функции2')
        func()
        print('После вызова функции2')
    return wrapper


@dec1
@dec2
def hello():
    print("Привет!")


hello()