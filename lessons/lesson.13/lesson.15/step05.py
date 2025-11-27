import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s - %(asctime)s - %(name)s - %(message)s - %(filename)s ',
)


logger_main = logging.getLogger('main')
logger_data = logging.getLogger('data')


def demo():
    logger_main.debug('Это DEBUG сообщение 2')
    logger_main.info('Это информационное сообщение 2' )
    logger_main.warning('Это WARNING сообщение 2')


logger_data.error('Это EROOR сообщение 2')
logger_data.critical('Это CRITICAL сообщение 2')
demo()