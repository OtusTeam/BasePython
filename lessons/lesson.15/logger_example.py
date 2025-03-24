import random

'''
for i in range(100):
    random_int = random.randint(1, 10)
    if 0 <= random_int <= 1:
        print("Пользователь вошел на сайт")
    elif 2 <= random_int <= 3:
        print("Пользователь купил товар")
    elif 4 <= random_int <= 5:
        print(f"Отладочный {random_int=}")
    elif 6 <= random_int <= 7:
        print('Критическая ошибка')
    elif 8 <= random_int <= 9:
        print('Предупреждение о таймауте')
    elif 9 <= random_int <= 10:
        print('Ошибка')
'''

'''
import logging

logging.basicConfig(level=logging.CRITICAL, format='%(asctime)s [%(levelname)s] %(message)s', filename='mylogs.log')


for i in range(100):
    random_int = random.randint(1, 10)
    if 0 <= random_int <= 1:
        logging.info("Пользователь вошел на сайт")
    elif 2 <= random_int <= 3:
        logging.info("Пользователь купил товар")
    elif 4 <= random_int <= 5:
        logging.debug(f"Отладочный {random_int=}")
    elif 6 <= random_int <= 7:
        try:
            raise ValueError('Информация об ошибке')
        except ValueError as e:
            logging.critical(f'Критическая ошибка {e}')
    elif 8 <= random_int <= 9:
        logging.warning('Предупреждение о таймауте')
    elif 9 <= random_int <= 10:
        logging.error('Ошибка')
'''

import logging

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('custom.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

for i in range(100):
    random_int = random.randint(1, 10)
    if 0 <= random_int <= 1:
        logger.info("Пользователь вошел на сайт")
    elif 2 <= random_int <= 3:
        logger.info("Пользователь купил товар")
    elif 4 <= random_int <= 5:
        logger.debug(f"Отладочный {random_int=}")
    elif 6 <= random_int <= 7:
        try:
            raise ValueError('Информация об ошибке')
        except ValueError as e:
            logger.critical(f'Критическая ошибка {e}')
    elif 8 <= random_int <= 9:
        logger.warning('Предупреждение о таймауте')
    elif 9 <= random_int <= 10:
        logger.error('Ошибка')
