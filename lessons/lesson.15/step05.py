import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    filename='step05.log',
    filemode='a'
)


def main():
    logging.info('hello world')


main()
logging.error('Это ошибка вне функции')