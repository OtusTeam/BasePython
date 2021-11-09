import asyncio
import logging
from dataclasses import dataclass
from typing import Optional, Union

from aiohttp import ClientSession

DEFAULT_FORMAT = "%(asctime)s %(levelname)-8s [%(name)-8s] (%(filename)s:%(funcName)s:%(lineno)d) %(message)s"

logging.basicConfig(format=DEFAULT_FORMAT, level=logging.DEBUG)

log = logging.getLogger(__name__)


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


async def fetch_ip(service: Service) -> Optional[str]:
    log.info("Fetch ip from service %r", service.name)

    async with ClientSession() as session:
        json_data = await fetch_json(session, service.url)

    log.info("Fetched json from service %r: %s", service.name, json_data)

    return json_data.get(service.field)


async def get_my_ip(timeout: Union[int, float] = 1) -> Optional[str]:
    my_ip = None

    tasks = {
        # fetch_ip(service)  # deprecated!
        asyncio.create_task(fetch_ip(service))
        for service in SERVICES
    }

    coro = asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    done, pending = await coro

    for pending_task in pending:
        pending_task.cancel()
        log.info("Cancelled task %s", pending_task)

    for task in done:
        my_ip = task.result()
        break
    else:
        log.warning("Could not fetch ip, no completed tasks!")

    return my_ip


async def run_main():
    # for service in SERVICES:
    #     res = await fetch_ip(service)
    #     log.info("result for %r: %s", service.name, res)
    res = await get_my_ip(.15)
    log.info("My ip is %r", res)
    return res


def main():
    res = asyncio.run(run_main())
    log.info("finished main with result %r", res)


if __name__ == '__main__':
    main()
