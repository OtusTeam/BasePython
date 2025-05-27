import logging


logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s',
    filename='step4.log',
    filemode='a'

)


def main1():

    logging.debug('Это дебаг')
    logging.info('Это Информация')
    logging.warning('Это предупреждение')
    logging.error('Это ошибка')
    logging.critical('Это ошибка')


if __name__ == '__main__':
    main1()