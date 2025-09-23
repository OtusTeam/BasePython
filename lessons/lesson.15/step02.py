import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)s - %(funcName)s- %(message)s',
    filename='step02.log',
    filemode='w'
)


def demo():
    logging.info('это в функции demo')


demo()
logging.info('Это информационное сообщение')
logging.warning('Это предупреждение')
logging.error('Это ошибка')
logging.critical('Это критическая ошибка')