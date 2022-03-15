def demo_zip():
    for a, b in zip(range(5, 10), range(10, 20, 2)):
        print(a, b)


def demo_map():
    print(pow(2, 3))
    for i in map(pow, [2, 3, 4], [7, 5, 3]):
        print("i =", i)


def demo_walrus():
    a = ["spam", "eggs", "foobar"]
    # a = []
    # if len(a) > 0:
    #     print("a > 0, =", len(a))
    # a_len = len(a)
    # if a_len:
    #     print("a > 0, =", a_len)
    if a_len := len(a):
        print("a > 0, =", a_len)
    # if (a_len := len(a)) > 0:
    #     print("a > 0, =", a_len)
    else:
        print("no items in a")

    a = b = c = 42
    assert a == 42
    assert b == 42
    assert c == 42
    assert a == b == c == 42
    assert 40 < a < 50


def main():
    # demo_zip()
    # demo_map()
    demo_walrus()


if __name__ == "__main__":
    main()
