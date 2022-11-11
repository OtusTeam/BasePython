import asyncio
import logging

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def get_users():
    logger.info('started get_users')
    await asyncio.sleep(1)
    logger.info('finished get_users')


async def get_products():
    logger.info('started get_products')
    await asyncio.sleep(1.5)
    logger.info('finished get_products')


async def main():
    # await get_users()
    # await get_products()
    await asyncio.gather(get_users(), get_products())


if __name__ == '__main__':
    asyncio.run(main())
