import asyncio
import logging
from dataclasses import dataclass

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin-ssl", url="https://httpbin.org/get", field="origin"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    # Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="pie.dev", url="https://pie.dev/get", field="origin"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if log.isEnabledFor(logging.DEBUG):
                log.debug(
                    "Response status: %s, text: %s",
                    response.status,
                    await response.text(),
                )
            return await response.json()


async def fetch_ip_from_service(service: Service) -> str:
    log.info("Fetching IP address from %r", service.name)
    ip_address = ""
    try:
        data: dict = await fetch_api(service.url)
    except aiohttp.ClientError as ex:
        log.error("Failed to fetch ip from service %r, error: %s", service.name, ex)
        return ip_address
    ip_address = data and data.get(service.field) or ""
    log.info("Got ip %r from service %r", ip_address, service.name)
    return ip_address


async def fetch_my_ip_from_fastest(timeout: float = 1) -> str:
    tasks = {
        asyncio.create_task(
            fetch_ip_from_service(service=service),
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
        log.info("Task %r cancelled", task.get_name())

    for task in done:
        if ex := task.exception():
            log.warning("Task %r failed %r", task.get_name(), ex)
            continue

        result: str = task.result()
        log.info("Got result %r from task %r", result, task.get_name())
        return result

    log.warning("No result found")
    return ""


async def find_my_ip():
    log.info("Finding my IP address")
    my_ip = await fetch_my_ip_from_fastest()
    log.info("Finished getting my IP address")
    return my_ip


def main():
    configure_logging()
    log.info("Starting step async io http")

    ip_addr = asyncio.run(find_my_ip())
    log.info("My IP: %s", ip_addr)
    log.info("Finished main")


if __name__ == "__main__":
    main()