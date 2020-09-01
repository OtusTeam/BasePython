import asyncio
from dataclasses import dataclass
from functools import wraps
from timeit import default_timer

from aiohttp import ClientSession
from loguru import logger


def timing_dec(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        start_time = default_timer()
        func_result = await func(*args, **kwargs)
        end_time = default_timer()
        logger.info('Function execution time with args {}  is {:.4f}', args, end_time - start_time)
        return func_result
    return wrapper


@dataclass
class Service:
    name: str
    url: str
    ip_field: str


SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


@timing_dec
async def fetch_ip(service: Service) -> str:
    """
    :param service:
    :return:
    """
    # my_ip = "not found"
    async with ClientSession() as session:
        result = await fetch(session, service.url)


    logger.info("Got result for {}, result {}", service.name, result)
    # my_ip = result[service.ip_field]
    return result[service.ip_field]


async def get_my_ip():
    # res = await fetch_ip(SERVICES[0])

    done, pending = await asyncio.wait(
        [fetch_ip(s) for s in SERVICES],
        timeout=3,
        # return_when=asyncio.ALL_COMPLETED,
        return_when=asyncio.FIRST_COMPLETED,
    )
    # print(done)
    # print(pending)

    for t in pending:
        logger.debug("Cancelling task {}", t)
        t.cancel()

    my_ip = None
    for t in done:
        my_ip = t.result()
        break
    else:
        logger.warning("No results!")

    logger.info("Got my ip! {}", my_ip)


def run_main():
    asyncio.run(get_my_ip())


if __name__ == '__main__':
    run_main()
