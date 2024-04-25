class ClientError(Exception):
    status_code = 400
    message = 'Client error'


class ServerError(Exception):
    pass


def hello_handler(greeting):
    print(f'{greeting}!')


def sum_handler(x, y):
    print(f'{x} + {y} = {x + y}')


def handler(callback, *args):
    try:
        return callback(*args)
    except Exception as e:
        # 40x, 50x
        print(type(e), e)
        exit(1)


def main():
    handler(hello_handler, 'Hi')
    handler(sum_handler, 2, 3)
    handler(sum_handler, 2, '3')


main()
