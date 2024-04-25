import logging

# logging.basicConfig(...)
logger = logging.getLogger(__name__)


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
    except TypeError as e:
        # logger.exception(e)
        # logger.warning(e)
        logger.debug(e)
        print(...)
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
        # raise ServerError('div_handler')
        raise ServerError


def handler(callback, *args):
    try:
        return callback(*args)
    except ClientError as e:
        print('client error')
        # exit(4)
    except ServerError as e:
        print(
            f'server error: {e.args and e.args[0]}'
        )
        # print(dir(e))
        # print(e.args)
        # exit(5)
    except Exception as e:
        print(type(e), e)


def main():
    handler(hello_handler, 'Hi')
    handler(sum_handler, 2, 3)
    handler(sum_handler, 2, '3')
    handler(div_handler, 4, 2)
    handler(div_handler, 4, '2')
    handler(div_handler, 4, 0)


main()
