import logging


# logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logging.debug('debug')
logging.info('Это информационное сообщение')
logging.warning('Это предупреждение')
logging.error('Это ошибка')
logging.critical('Это серьезная ошибка')