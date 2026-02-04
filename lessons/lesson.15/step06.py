import logging


# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s - %(name)s - %(message)s - %(filename)s - %(lineno)s',
# )

logger_main = logging.getLogger("main")
logger_main.setLevel(logging.INFO)

file_handler = logging.FileHandler('step06.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.WARNING)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logger_main.addHandler(file_handler)
logger_main.addHandler(console_handler)

logger_main.info('Это информационное сообщение')
logger_main.warning('Это предупреждение')
logger_main.error('Это сообщение об ошибке')
logger_main.critical('Это сообщение об критической ошибке')