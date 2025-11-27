import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s - %(filename)s ',
    filename='step04.log',
    filemode='w'
)


def demo():
    logging.debug('Это DEBUG сообщение 2')
    logging.info('Это информационное сообщение 2' )
    logging.warning('Это WARNING сообщение 2')


logging.error('Это EROOR сообщение 2')
logging.critical('Это CRITICAL сообщение 2')
demo()