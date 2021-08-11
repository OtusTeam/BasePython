import asyncio
from dataclasses import dataclass

from aiohttp import ClientSession
from loguru import logger


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service("ipify", "https://api.ipify.org/?format=json", "ip"),
    Service("ip-api", "http://ip-api.com/json", "query"),
]


async def fetch_json(session: ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        return await response.json()


async def fetch_ip(service: Service) -> str:
    logger.info("Fetch ip from {}", service.name)

    async with ClientSession() as session:
        result = await fetch_json(session, service.url)

    logger.info("Fetched json from {!r}: {}", service.name, result)

    return result.get(service.field)


async def get_my_ip(timeout: int) -> str:
    my_ip = ""
    tasks = {
        # fetch_ip(service) # old python
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }
    coro = asyncio.wait(
        tasks,  # only tasks!
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    done_tasks, pending_tasks = await coro
    for pending_task in pending_tasks:
        pending_task.cancel()
        logger.info("Cancelled task {}", pending_task)

    for task in done_tasks:
        my_ip = task.result()
        break
    else:
        logger.warning("Could not fetch ip!")

    logger.info("Done fetching, returning {!r}", my_ip)
    return my_ip


async def query_services():
    for service in SERVICES:
        ip = await fetch_ip(service)
        logger.info("My ip by {} is {}", service.name, ip)


def main():
    logger.info("Starting main")
    my_ip = asyncio.run(get_my_ip(1))
    logger.info("Got ip: {!r}", my_ip)
    logger.info("Finishing main")


if __name__ == '__main__':
    main()
