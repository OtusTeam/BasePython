import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s - %(filename)s - %(funcName)s - %(lineno)s - %(module)s',
)


def demo():
    logging.debug('Это DEBUG сообщение')
    logging.info('Это информационное сообщение')
    logging.warning('Это WARNING сообщение')


logging.error('Это EROOR сообщение')
logging.critical('Это CRITICAL сообщение')
demo()