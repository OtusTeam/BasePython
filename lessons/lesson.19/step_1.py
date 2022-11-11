import logging
from time import sleep

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')

logger = logging.getLogger(__name__)


def get_users():
    logger.info('started get_users')
    sleep(1)
    logger.info('finished get_users')


def get_products():
    logger.info('started get_products')
    sleep(1.5)
    logger.info('finished get_products')


get_users()
get_products()
