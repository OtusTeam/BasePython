import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s: - %(name)s - %(filename)s - строка: %(lineno)s - %(funcName)s - %(message)s ',
    filename='app.log',
    filemode='a'
    # filemode='w'
)


def demo():
    logging.debug('Это debug сообщение')


logging.info('Это информационное сообщение')
logging.warning('Это предупреждение')
logging.error('Это сообщение об ошибке')
logging.critical('Это сообщение об критической ошибке')
demo()