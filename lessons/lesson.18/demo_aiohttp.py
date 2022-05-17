import asyncio
from dataclasses import dataclass
from typing import Optional

import aiohttp
from loguru import logger


async def demo_query_httpbin():
    async with aiohttp.ClientSession() as session:
        async with session.get('https://httpbin.org/get') as resp:
            print(resp.status)
            print(await resp.text())
            print(await resp.json())


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
]

# def find_my_ip():
#     for service in SERVICES:
#         try:
#             my_ip = get_my_ip_sync(service)
#             if is_ok(my_ip):
#                 return my_ip
#         except Exception:
#             ...


async def fetch_json(session: aiohttp.ClientSession, url: str) -> dict:
    async with session.get(url) as response:
        data: dict = await response.json()
        logger.info("got response for {} with status {} and data {}", url, response.status, data)
        return data


async def fetch_ip(service: Service) -> Optional[str]:
    logger.info("fetch ip from {!r}", service.name)

    # session = aiohttp.ClientSession()
    # async with aiohttp.ClientSession() as session
    # async with session as session
    # async with session:
    #     pass

    # await session.close()

    async with aiohttp.ClientSession() as session:
        data = await fetch_json(session, service.url)
        return data.get(service.field)


async def get_my_ip(timeout=0.5) -> str:
    logger.info("searching for ip")
    tasks = {
        asyncio.create_task(fetch_ip(service), name=service.name)
        for service in SERVICES
    }
    coro = asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    done, pending = await coro

    for task in pending:  # type: asyncio.Task
        task.cancel()
        logger.info("Cancelled task {}", task)

    my_ip = ""
    for task in done:
        my_ip = task.result()
        break
    else:
        logger.warning("Could not fetch IP!")

    logger.info("Finishing with IP {!r}", my_ip)
    return my_ip


async def demo_gather_results():
    async with aiohttp.ClientSession() as session:
        httpbin_result, service_0_result, service_1_result = await asyncio.gather(
            fetch_json(session, "https://httpbin.org/get"),
            fetch_json(session, SERVICES[0].url),
            fetch_json(session, SERVICES[1].url),
        )

    logger.info("httpbin {}", httpbin_result)
    logger.info("s0 {}", service_0_result)
    logger.info("s1 {}", service_1_result)


if __name__ == '__main__':
    # asyncio.run(demo_gather_results())

    ip = asyncio.run(get_my_ip(timeout=0.15))
    logger.info("done, ip {!r}", ip)
