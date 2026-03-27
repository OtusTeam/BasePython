import asyncio
import logging
from dataclasses import dataclass
from typing import Any

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class IpService:
    name: str
    url: str
    field: str


SERVICES = [
    IpService(
        name="httpbin-http",
        url="http://httpbin.org/get",
        field="origin",
    ),
    IpService(
        name="httpbin-https",
        url="https://httpbin.org/get",
        field="origin",
    ),
    IpService(
        name="pie.dev",
        url="https://pie.dev/get",
        field="origin",
    ),
    IpService(
        name="ip-api",
        url="http://ip-api.com/json",
        field="query",
    ),
    IpService(
        name="ipify",
        url="https://api.ipify.org/?format=json",
        field="ip",
    ),
]


async def fetch_api(
    url: str,
) -> dict[str, Any]:

    log.info("Fetching data from %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()

    log.info("Got data from %s: %s", url, result)
    return result


async def get_ip_from_service(
    service: IpService,
) -> str:
    log.info("Fetching data from %s", service.name)
    data = await fetch_api(service.url)
    ip_address = data.get(service.field) or ""
    log.info(
        "Got data from %s: %r",
        service.name,
        ip_address,
    )
    return ip_address


async def fetch_ip_fastest(
    services: list[IpService],
    timeout: float = 1,
) -> str:
    if not services:
        log.info("No services found")
        return ""

    tasks = {
        asyncio.create_task(
            get_ip_from_service(service),
            name=f"get-ip-from-{service.name!r}",
        )
        for service in services
    }
    log.info("Fetching data using %d tasks", len(tasks))

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:
        log.info(
            "cancelling task %s",
            task.get_name(),
        )
        task.cancel()

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        # result = await task
        result = task.result()
        log.info(
            "Task %r completed with result %r",
            task.get_name(),
            result,
        )
        if result:
            return result

    log.error("No IP fetched!")
    return ""


async def main():
    configure_logging()
    log.info("Starting")

    my_ip = await fetch_ip_fastest(
        SERVICES,
        timeout=0.2,
    )
    log.info("Got IP: %r", my_ip)
    log.info("Finishing")
    return my_ip


if __name__ == "__main__":
    ip_result = asyncio.run(main())
    print(ip_result)
