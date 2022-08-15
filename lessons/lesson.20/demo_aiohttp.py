import asyncio
from dataclasses import dataclass

import aiohttp
from loguru import logger


@dataclass(frozen=True)
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="httpbin-secure", url="https://httpbin.org/get", field="origin"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


# from typing import Optional
# async def fetch_ip(service: Service) -> Optional[str]:


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:  # type: aiohttp.ClientResponse
        data = await response.json()
        return data


async def fetch_ip(service: Service) -> str | None:
    logger.info("fetch service {}", service.name)

    # session = aiohttp.ClientSession()
    # session.get(...)
    # await session.close()
    async with aiohttp.ClientSession() as session:
        data: dict = await fetch_json(session, service.url)
        logger.info("done for service {}", service.name)
        return data.get(service.field)


# from typing import Union
# Union[int, float]

async def get_my_ip(timeout: int | float = 0.5) -> str:
    logger.info("Search for my ip")
    my_ip = ""

    tasks = {
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    # logger.info("done {}", done)
    # logger.info("pending {}", pending)

    for task in pending:  # type: asyncio.Task
        task.cancel()
    # logger.info("pending {}", pending)

    for task in done:  # type: asyncio.Task
        my_ip = task.result()
        break
    else:
        logger.warning("could not find ip!")

    logger.info("Fetched ip {}", my_ip)
    return my_ip


def main():
    logger.info("Start ip fetch")
    ip = asyncio.run(get_my_ip())
    logger.info("Finish ip fetch with result {!r}", ip)


if __name__ == '__main__':
    main()
