import asyncio
import logging
from dataclasses import dataclass

import aiohttp
from common import configure_logging

log = logging.getLogger(__name__)


@dataclass(frozen=True)
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin-ssl", url="https://httpbin.org/get", field="origin"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    Service(name="httpbin", url="http://httpbin.org/", field="origin"),
    Service(name="pie.dev", url="https://pie.dev/get", field="origin"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def fetch_api(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()


async def fetch_ip_from_service(service: Service) -> str:
    log.info("Fetch ip from service: %s", service.name)
    data: dict = await fetch_api(url=service.url)
    ip_address: str = data and data.get(service.field) or ""
    log.info("got ip %r from service: %s", ip_address, service.name)
    return ip_address


async def find_my_ip(timeout: float = 1) -> str:
    tasks = {
        asyncio.create_task(
            fetch_ip_from_service(service),
            name=f"service-{service.name}",
        )
        for service in SERVICES
    }
    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        task.cancel()
        log.debug("task %r cancelled", task.get_name())

    for task in done:
        result = task.result()
        log.info("task %r result: %r", task.get_name(), result)
        return result

    log.warning("Couldn't get any data")
    return ""

    # for task in done:
    #     result = task.result()
    #     break
    # else:
    #     log.warning("Couldn't get any data")
    #
    # return ""


async def async_main() -> None:
    my_ip = await find_my_ip()
    log.info("My ip: %s", my_ip)


def main():
    configure_logging()
    asyncio.run(async_main())
    my_ip = asyncio.run(find_my_ip())
    log.info("My ip: %s", my_ip)


if __name__ == "__main__":
    main()
