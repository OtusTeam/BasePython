import asyncio
import logging
from dataclasses import dataclass
from random import random
from time import sleep

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
    Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="pie.dev", url="https://pie.dev/get", field="origin"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def fetch_api(url: str) -> dict:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip_from_service(service: Service) -> str:
    log.info("Fetch IP from service %r", service.name)

    try:
        data: dict = await fetch_api(service.url)
    except aiohttp.ClientError as ex:
        log.info(
            "Could not fetch ip from service %r, got error: %s",
            service.name,
            ex,
        )
        return ""

    ip_address = data and data.get(service.field) or ""
    log.info("Got ip %r from service %r", ip_address, service.name)
    return ip_address


async def fetch_my_ip_from_fastest(timeout: float = 1) -> str:
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
        log.info("Task %r cancelled", task.get_name())

    for task in done:
        if error := task.exception():
            log.warning("Task %r failed, error: %s", task.get_name(), error)
            continue

        result: str = task.result()
        log.info("Got ip %r from task %r", result, task.get_name())
        return result

    log.warning("No result found")
    return ""


async def fetch_my_ip() -> str:
    log.info("Start main 09 wait for ip")
    result = await fetch_my_ip_from_fastest()
    log.info("Finished main 09 wait for ip")
    return result


def main() -> None:
    configure_logging()
    ip = asyncio.run(fetch_my_ip())
    log.info("finally my ip: %r", ip)


if __name__ == "__main__":
    main()
