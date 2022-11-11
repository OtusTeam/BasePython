import logging
import asyncio
from dataclasses import dataclass

import aiohttp

logging.basicConfig(format='%(asctime)s.%(msecs)03d %(message)s',
                    level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S')
logging.getLogger('asyncio').setLevel(logging.WARNING)
logger = logging.getLogger(__name__)


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="httpbin-secure", url="https://httpbin.org/get", field="origin"),
    # Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    # Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def get_my_ip(svc):
    logger.info('try "%s": %s', svc.name, svc.url)
    async with aiohttp.ClientSession() as session:
        response = await session.get(svc.url)
        data = await response.json()
        my_ip = data.get(svc.field)
        logger.info('done "%s": %s', svc.name, my_ip)
        return my_ip


async def main():
    logger.info('started')
    tasks = {asyncio.create_task(get_my_ip(el))
             for el in SERVICES}

    done, pending = await asyncio.wait(
        tasks,
        timeout=0.9,
        return_when=asyncio.FIRST_COMPLETED
    )
    logger.info('done %d, pending %d', len(done), len(pending))
    for el in done:
        logger.info(el.result())
        break
    else:
        logger.warning('smth wrong')

    for el in pending:
        # logger.warning(el)
        el.cancel()

    # for el in pending:
    #     logger.warning(el)


if __name__ == '__main__':
    asyncio.run(main())
