import logging


logging.basicConfig(
    # level=logging.INFO,
    # format='%(asctime)s - %(name)s - %(levelname)s - %(filename)s - %(lineno)s - %(funcName)s- %(message)s',
    # filename='step02.log',
    # filemode='w'
)


logger_main = logging.getLogger('main')
# logger_main.setLevel(logging.ERROR)
logger_data = logging.getLogger('data')

# Создаём хэндлер для файла
file_handler = logging.FileHandler('step03.log', mode='w', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

# Формат для файла
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)

# Создаем хэндлер для консоли
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

logger_main.addHandler(file_handler)
logger_main.addHandler(console_handler)

logger_data.addHandler(console_handler)


# logger_main.info('Это информационное сообщение')
# # logger_data.warning('Это предупреждение')
# logger_main.error('Это ошибка')
# logger_data.critical('Это критическая ошибка')

logger_main.error('Это информационное сообщение')
