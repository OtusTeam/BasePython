# 1 / 0
# print("never!")

# print(ZeroDivisionError, ZeroDivisionError.mro())
# print(TypeError, TypeError.mro())
# raise Exception

def call_exc():
    exc = Exception("unexpected error!")
    raise exc


def another():
    raise ValueError
    call_exc()


def main():
    call_exc()


if __name__ == '__main__':
    another()
    main()
    print("never!")
