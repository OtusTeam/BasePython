import logging


logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(filename)s - %(lineno)s - %(funcName)s'
)



def demo():
    logging.debug('Это debug сообщение')


demo()
logging.info('Это информационное сообщение')
logging.warning('Это предупреждение')
logging.error('Это сообщение об ошибке')
logging.critical('Это сообщение об критической ошибке')