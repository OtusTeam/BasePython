import asyncio
from dataclasses import dataclass
from http import HTTPStatus

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    ip_field: str

# https://api.ipify.org/?format=json
# http://ip-api.com/json


SERVICES = [
    # Service("ipify", "https://api.ipify.org/qwerty/?format=json", "ip"),
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        # if (status_code := response.status) != HTTPStatus.OK:
        #     logger.error("[status: {}] Could not fetch url {!r}", status_code, response.url)
        #     return {}
        return await response.json()


async def fetch_ip(service: Service) -> str:
    logger.info("Fetch ip from {}", service.name)

    # session = ClientSession()
    # await session.close()
    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched {}. Result: {}", service.name, result)

    return result.get(service.ip_field)


async def get_my_ip(timeout=0.1, last_try=False) -> str:
    logger.info("Start getting my IP")

    my_ip = ""

    tasks = {
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }

    coro = asyncio.wait(
        tasks,
        timeout=timeout,
        # timeout=5,
        return_when=asyncio.FIRST_COMPLETED,
        # return_when=asyncio.ALL_COMPLETED,
    )
    # a = True
    # b = False
    # return a and b

    done, pending = await coro
    if not done and not last_try:
        logger.info("try again")
        # 1
        # result = await get_my_ip(timeout * 10, last_try=True)
        # return result
        # 2
        # return (await get_my_ip(timeout * 10, last_try=True))
        # 3
        return await get_my_ip(timeout * 10, last_try=True)

    for task in pending:
        task.cancel()
        logger.info("Cancelled task {}", task)

    for task in done:
        my_ip = task.result()
        break
    else:
        logger.warning("Could not fetch IP!")

    logger.info("Finish getting my IP")
    return my_ip


def main():
    result = asyncio.run(get_my_ip())
    logger.info("RESULT: {}", result)


if __name__ == "__main__":
    main()
