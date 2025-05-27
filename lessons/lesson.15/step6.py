import logging


# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
#     filename='step5.log',
#     filemode='a'
#
# )
logger_main = logging.getLogger('main')
logger_main.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('step6.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.ERROR)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)


console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')
console_handler.setFormatter(console_formatter)


logger_main.addHandler(file_handler)
logger_main.addHandler(console_handler)



def main():

    logger_main.debug('Это дебаг')
    logger_main.info('Это Информация')
    logger_main.warning('Это предупреждение')
    logger_main.error('Это ошибка')
    logger_main.critical('Это ошибка')


if __name__ == '__main__':
    main()