import asyncio
import logging
from dataclasses import dataclass
from typing import Any

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class IpInfoService:
    name: str
    url: str
    field: str


SERVICES = [
    IpInfoService(name="httpbin-ssl", url="https://httpbin.org/get", field="origin"),
    IpInfoService(name="ip-api", url="http://ip-api.com/json", field="query"),
    IpInfoService(name="httpbin", url="http://httpbin.org/get", field="origin"),
    # IpInfoService(name="pie.dev", url="https://pie.dev/get", field="origin"),
    # IpInfoService(name="pie.dev-post", url="https://pie.dev/post", field="origin"),
    IpInfoService(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def fetch_api(url: str) -> dict[str, Any]:
    async with aiohttp.ClientSession(raise_for_status=True) as session:
        async with session.get(url) as response:
            return await response.json()


async def fetch_ip_from_service(service: IpInfoService) -> str:
    log.info("Fetching IP from service %r", service.name)
    try:
        data: dict[str, str] = await fetch_api(service.url)
    except aiohttp.ClientError as ex:
        log.error("Failed to fetch IP from service %r: %s", service.name, ex)
        raise ex
    ip_address = data.get(service.field) or ""
    log.info("IP %r from service %r", ip_address, service.name)
    return ip_address


async def fetch_ip_fastest(timeout: float = 0.9) -> str:
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
        log.info("Gonna cancel task: %s", task)
        task.cancel()
        log.info("Cancelled task: %s", task)

    log.info("done tasks: %s", done)
    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        my_ip = task.result()
        log.info("IP %r from %r", my_ip, task.get_name())
        return my_ip

    log.warning("No results fetched")
    return ""


async def main():
    configure_logging()

    log.warning("Starting 09")

    my_ip = await fetch_ip_fastest()

    log.warning("Finished 09")

    return my_ip


if __name__ == "__main__":
    result = asyncio.run(main())
    log.info("Result: %r", result)
