import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession, ClientResponse

from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service("ip-api", "http://ip-api.com/json", "query"),
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    logger.info("fetch url {}", url)
    async with session.get(url) as response:  # type: ClientResponse
        response_json = await response.json()
        logger.info("fetched url {} and got data {}", response.url, response_json)
        return response_json


async def fetch_ip(service: Service) -> str:
    async with ClientSession() as session:
        data = await fetch_json(session, service.url)
    # session = ClientSession()
    # data = await fetch_json(session, service.url)
    # await session.close()

    logger.info("got data for service {}: {}", service.name, data)
    return data.get(service.field, "")


async def get_my_ip(timeout: float = 1) -> str:
    my_ip = ""
    tasks = {
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }
    logger.info("start processing tasks")

    coro = asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    # a, b = await coro
    done_tasks, pending_tasks = await coro
    for pending_task in pending_tasks:
        pending_task.cancel()
        logger.info("Cancelled task {}", pending_task.get_name())

    for task in done_tasks:
        my_ip = task.result()
        break
    else:
        logger.warning("could not fetch ip")

    logger.info("done fetching ip: {}", my_ip)

    return my_ip


async def main():
    logger.info("Start main")
    my_ip = await get_my_ip(timeout=0.3)
    return my_ip


def main_sync():
    ip = asyncio.run(main())
    logger.info("result: {}", ip)


if __name__ == "__main__":
    main_sync()
