import one


# from one import hello_one


def hello_two():
    print('two')


def smth():
    from one import hello_one

    hello_one()


# one.hello_one()
