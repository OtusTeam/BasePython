import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: - %(name)s - %(filename)s - строка: %(lineno)s - %(funcName)s - %(message)s ',
)

logger_main = logging.getLogger('main')
logger_data = logging.getLogger('data')


def demo():
    logging.error('Это error сообщение от root')


logger_main.info('Это информационное сообщение logger_main')
logger_data.warning('Это предупреждение logger_data')
logger_main.error('Это сообщение об ошибке logger_main')
logger_data.critical('Это сообщение logger_data об критической ошибке')
demo()