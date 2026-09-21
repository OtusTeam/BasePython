def outer(name):
    def inner():
        print(f'Привет, {name}')
    return inner


hello_ivan1 = outer('ivan1')
hello_ivan2 = outer('ivan2')

print(hello_ivan1)
print(type(hello_ivan1))



hello_ivan3 = outer('oleg')
print(hello_ivan3)
print(type(hello_ivan3))


hello_ivan1()
hello_ivan2()
hello_ivan3()