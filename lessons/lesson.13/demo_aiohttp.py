import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    ip_field: str


SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    """
    :param service:
    :return:
    """
    logger.info("Fetching {}", service.name)
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched {}, result: {}", service.name, result)

    # if service.name == "ip-api":
    #     logger.info("sleeping for ip-api")
    #     await asyncio.sleep(5)

    return result[service.ip_field]


async def get_my_ip():
    # service = SERVICES[0]
    # service = SERVICES[1]

    # my_ip = await fetch_ip(service)

    coro = asyncio.wait(
        {
            asyncio.create_task(fetch_ip(service))
            for service in SERVICES
        },
        timeout=5,
        return_when=asyncio.FIRST_COMPLETED,
    )

    done, pending = await coro

    for task in pending:
        logger.debug("Cancelling task {}", task)
        task.cancel()

    my_ip = None
    for task in done:
        my_ip = task.result()
        break
    else:
        logger.warning("No results found!")

    # logger.info("Gor results: {}", results)
    logger.info("My ip: {!r}", my_ip)
    return my_ip


def run_main():
    logger.info("Starting")
    result = asyncio.run(get_my_ip())
    logger.info("Result: {}", result)


if __name__ == "__main__":
    run_main()
