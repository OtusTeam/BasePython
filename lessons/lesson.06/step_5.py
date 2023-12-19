def foo():
    # raise ValueError
    # raise ValueError()
    raise ValueError("invalid data")


def bar():
    try:
        # foo()
        1 / 0
    except Exception as e:
        print(type(e), repr(e), e)


def main():
    try:
        foo()
    except ValueError as e:
        print(type(e), repr(e), e)


main()
