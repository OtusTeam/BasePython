import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
    filename='step5.log',
    filemode='a'

)

logger_main = logging.getLogger('main')
logger_data = logging.getLogger('data')


def main1():

    logger_data.debug('Это дебаг')
    logger_main.info('Это Информация')
    logger_data.warning('Это предупреждение')
    logger_main.error('Это ошибка')
    logger_data.critical('Это ошибка')


if __name__ == '__main__':
    main1()