import logging


logger_main = logging.getLogger('main')
logger_main.setLevel(logging.DEBUG)


logger_data = logging.getLogger('data')
logger_data.setLevel(logging.INFO)


file_handler = logging.FileHandler('step06.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.WARNING)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logger_main.addHandler(file_handler)
logger_main.addHandler(console_handler)

logger_data.addHandler(file_handler)


logger_main.debug('Это DEBUG сообщение 3')
logger_main.info('Это информационное сообщение 3' )
logger_main.warning('Это WARNING сообщение 3')
logger_main.error('Это EROOR сообщение 3')
logger_main.critical('Это CRITICAL сообщение 3')
logger_data.critical('Это CRITICAL сообщение 3')
