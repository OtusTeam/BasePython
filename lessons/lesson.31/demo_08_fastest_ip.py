import asyncio
import logging
from dataclasses import dataclass
from typing import Any

import aiohttp

from logging_config import configure_logging

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
    # IpService(
    #     name="pie.dev",
    #     url="https://pie.dev/get",
    #     field="origin",
    # ),
    IpService(
        name="ip-api",
        url="http://ip-api.com/json",
        field="query",
    ),
    # IpService(
    #     name="ipify",
    #     url="https://api.ipify.org/?format=json",
    #     field="ip",
    # ),
]


async def fetch_api(
    url: str,
) -> dict[str, str]:
    log.debug("Fetching %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    log.debug(
        "Fetched data from %s, result: %s",
        url,
        result,
    )
    return result


async def get_ip_from_service(
    service: IpService,
) -> str:
    log.info("Fetchin IP from %r", service.name)
    data = await fetch_api(service.url)
    ip_address = data.get(service.field) or ""
    log.info(
        "Fetched IP %r from service %r",
        ip_address,
        service.name,
    )
    return ip_address


async def fetch_ip_fastest(
    services: list[IpService],
    timeout: float = 1,
) -> str:
    if not services:
        log.warning("No services provided")
        return ""

    log.info(
        "Fetching IP from one of %d services",
        len(services),
    )
    tasks = {
        asyncio.create_task(
            get_ip_from_service(service),
            name=f"get-ip-from-{service.name!r}",
        )
        for service in services
    }
    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    log.debug("done: %d tasks", len(done))
    log.debug("pending: %d tasks", len(pending))

    for task in pending:
        log.debug(
            "cancelling task %r",
            task.get_name(),
        )
        task.cancel()

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        # result = task.result()
        result = await task
        log.info(
            "Task %r result: %r",
            task.get_name(),
            result,
        )
        if result:
            return result

    log.warning("No IP fetched!")
    return ""


async def main() -> str:
    configure_logging(level=logging.DEBUG)
    log.info("Starting")

    my_ip = await fetch_ip_fastest(SERVICES)
    log.info("My IP is: %r", my_ip)

    log.info("Finished")
    return my_ip


if __name__ == "__main__":
    ip = asyncio.run(main())
    log.info("The IP is: %r", ip)
