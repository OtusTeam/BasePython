import logging

import aiohttp
import asyncio

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


async def get_my_ip(url, field):
    logger.info('start %s', url)
    async with aiohttp.ClientSession() as session:
        response = await session.get(url)
        # data = response.json()  # coroutine obj
        data = await response.json()
        my_ip = data.get(field)
        logger.info('my ip %s', my_ip)
        return my_ip


def main():
    asyncio.run(get_my_ip('http://httpbin.org/get', 'origin'))


if __name__ == '__main__':
    main()
