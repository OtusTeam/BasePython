import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


logger_main = logging.getLogger('main')
logger_demo = logging.getLogger('demo')

def main():
    logger_main.info('hello world')


main()
logger_demo.error('Это ошибка вне функции')