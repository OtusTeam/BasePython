class ClientError(Exception):
    status_code = 400
    message = 'Client error'


class ServerError(Exception):
    pass


def hello_handler(greeting):
    print(f'{greeting}!')


def sum_handler(x, y):
    try:
        print(f'{x} + {y} = {x + y}')
    except TypeError:
        raise ClientError
    except Exception:
        raise ServerError


def div_handler(x, y):
    try:
        print(f'{x} / {y} = {x / y}')
    except TypeError as e:
        print(e)
        raise ClientError
    except Exception as e:
        print(e)
        raise ServerError


def handler(callback, *args):
    try:
        return callback(*args)
    except Exception as e:
        pass
        # 40x, 50x
        print(type(e), e)
        # exit(1)


def main():
    handler(hello_handler, 'Hi')
    handler(sum_handler, 2, 3)
    handler(sum_handler, 2, '3')
    handler(div_handler, 4, 2)
    handler(div_handler, 4, '2')
    handler(div_handler, 4, 0)


main()
