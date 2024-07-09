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
    Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="pie.dev", url="https://pie.dev/get", field="origin"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def fetch_api(url: str, params: dict | None = None) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            return await response.json()


async def fetch_ip_from_service(service: Service) -> str:
    log.info("Fetching ip from service %r", service.name)
    try:
        data: dict = await fetch_api(url=service.url)
    except aiohttp.ClientError as ex:
        log.error("Failed to fetch ip from service %r, error: %s", service.name, ex)
        return ""
    ip_address: str = data and data.get(service.field) or ""
    log.info("Got ip %r from service %r", ip_address, service.name)
    return ip_address


async def find_my_ip_from_fastest(timeout: float = 1) -> str:
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
        log.debug("Task %r cancelled", task.get_name())

    for task in done:
        if ex := task.exception():
            # log.warning("Error for task %r", task.get_name(), exc_info=ex)
            log.warning("Error for task %r, error text: %s", task.get_name(), ex)
            continue

        result: str = task.result()
        log.debug("Task %r result: %r", task.get_name(), result)
        return result

    log.warning("Could not get any data")
    return ""


async def find_my_ip():
    log.warning("Starting find_my_ip")

    # my_ip = await fetch_ip_from_service(service=SERVICES[0])
    # log.info("My ip: %s", my_ip)
    my_ip = await find_my_ip_from_fastest(timeout=0.2)
    log.info("My ip: %r", my_ip)

    log.warning("Finished find_my_ip")
    return my_ip


def main():
    configure_logging()
    ip = asyncio.run(find_my_ip())
    log.info("Finally, my ip: %r", ip)


if __name__ == "__main__":
    main()
