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
    return callback(*args)


def main():
    handler(hello_handler, 'Hi')
    handler(sum_handler, 2, 3)
    handler(sum_handler, 2, '3')


main()
