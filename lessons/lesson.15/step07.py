import logging


logging.basicConfig(
    # level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)


logger_main = logging.getLogger('main')
logger_demo = logging.getLogger('demo')

file_handler = logging.FileHandler('main.log', mode='a', encoding='utf-8')
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.ERROR)


logger_main.addHandler(console_handler)
logger_demo.addHandler(file_handler)

def main():
    logger_main.info('hello world')


main()
logger_demo.error('Это ошибка вне функции')