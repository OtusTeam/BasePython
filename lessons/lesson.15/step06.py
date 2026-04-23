import logging

# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(levelname)s: - %(name)s - %(filename)s - строка: %(lineno)s - %(funcName)s - %(message)s ',
# )

logger_main = logging.getLogger('main')
logger_main.setLevel(logging.DEBUG)
# logger_data = logging.getLogger('data')

file_handler = logging.FileHandler('app06.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.WARNING)
file_formatter = logging.Formatter('%(asctime)s - %(levelname)s: - %(name)s - %(filename)s - строка: %(lineno)s - %(message)s')
file_handler.setFormatter(file_formatter)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_formatter = logging.Formatter('- %(levelname)s: %(asctime)s  - %(name)s - строка: %(lineno)s - %(message)s')
console_handler.setFormatter(console_formatter)

logger_main.addHandler(file_handler)
logger_main.addHandler(console_handler)


def demo():
    logger_main.debug('Это error сообщение от root')


logger_main.info('Это информационное сообщение logger_main')
logger_main.warning('Это предупреждение logger_data')
logger_main.error('Это сообщение об ошибке logger_main')
logger_main.critical('Это сообщение logger_data об критической ошибке')
demo()