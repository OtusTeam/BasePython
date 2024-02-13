import asyncio
import logging
from dataclasses import dataclass

import aiohttp
import common

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin", url="https://httpbin.org/get", field="origin"),
    Service(name="pie.dev", url="https://pie.dev/get", field="origin"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
    # Service(name="ip-api", url="http://ip-api.com/json", field="query"),
]


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def get_ip_from_service(service: Service) -> str:
    log.info("Fetch ip from service %s", service.name)
    data: dict = await fetch_api(service.url)
    ip_address: str = data.get(service.field, "")
    log.info("got ip %r from service %r", ip_address, service.name)
    return ip_address


async def find_my_ip(timeout: float = 1) -> str:
    # await get_ip_from_service(SERVICES[0])
    # await get_ip_from_service(SERVICES[1])
    # await get_ip_from_service(SERVICES[2])

    return
    tasks = {
        asyncio.create_task(
            get_ip_from_service(service),
            name=f"service-{service.name}",
        )
        for service in SERVICES
    }

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:  # type: asyncio.Task
        task.cancel()
        log.debug("canceled task %s", task.get_name())

    result = ""
    for task in done:
        result = task.result()
        log.info("take result from task %s", task.get_name())
        break
    else:
        log.warning("Couldn't get any data")

    return result


def main():
    common.configure_logging()
    my_ip = asyncio.run(find_my_ip(timeout=0.8))
    log.warning("My ip: %r", my_ip)


if __name__ == "__main__":
    main()
