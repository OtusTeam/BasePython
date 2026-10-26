
no_name = sentinel("NONAME")

def hello(name: str = no_name):
    print("Hello", name)
    print(type(name))


if __name__ == '__main__':
    hello()
