import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(filename)s - %(lineno)s',
)

logger_main = logging.getLogger("main")
logger_data = logging.getLogger("data")



logger_main.info('Это информационное сообщение')
logger_data.warning('Это предупреждение')
logger_data.error('Это сообщение об ошибке')
logger_main.critical('Это сообщение об критической ошибке')