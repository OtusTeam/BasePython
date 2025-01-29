import asyncio

import logging
from dataclasses import dataclass
from typing import Any

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


async def fetch_api(url: str) -> dict[str, Any]:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip_from_service(service: Service) -> str:
    log.info("Fetch IP from service: %r", service.name)
    try:
        data: dict = await fetch_api(service.url)
    except aiohttp.ClientError as ex:
        log.error("Failed to fetch IP from service %r, error: %s", service.name, ex)
        return ""

    ip_addr = data and data.get(service.field) or ""
    log.info("Got IP %r from service %r", ip_addr, service.name)
    return ip_addr


async def fetch_my_ip_fastest(timeout: float = 0.8) -> str:
    log.info("Start fetching IP fastest")
    tasks = {
        asyncio.create_task(
            # fetch from each one
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
            log.warning(
                "Task %r failed with exception: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        my_ip: str = task.result()
        log.info("Got IP %r from task %r", my_ip, task.get_name())
        return my_ip

    log.warning("No result fetched")
    return ""


async def main() -> str:
    configure_logging()
    log.info("Starting main 08")
    ip_result = await fetch_my_ip_fastest()
    log.info("Finished main 08")
    return ip_result


if __name__ == "__main__":
    ip = asyncio.run(main())
    log.info("my ip: %r", ip)
