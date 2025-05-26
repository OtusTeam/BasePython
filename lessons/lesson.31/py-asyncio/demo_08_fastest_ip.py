import asyncio
import logging
from dataclasses import dataclass
from typing import Any

import aiohttp

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class IpInfoServiceData:
    name: str
    url: str
    field: str


SERVICES = [
    IpInfoServiceData(
        name="httpbin-https",
        url="https://httpbin.org/get",
        field="origin",
    ),
    IpInfoServiceData(
        name="httpbin-http",
        url="http://httpbin.org/get",
        field="origin",
    ),
    # IpInfoServiceData(
    #     name="pie-dev",
    #     url="https://pie.dev/get",
    #     # url="https://pie.dev/post",
    #     field="origin",
    # ),
    # IpInfoServiceData(
    #     name="ipify",
    #     url="https://api.ipify.org/?format=json",
    #     field="ip",
    # ),
    IpInfoServiceData(
        name="ip-api",
        url="http://ip-api.com/json",
        field="query",
    ),
]


async def fetch_api(url: str) -> Any:
    log.debug("Fetching %s", url)
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            result = await response.json()
    log.debug("got result from %s: %s", url, result)
    return result


async def fetch_ip_from_service(service: IpInfoServiceData) -> str:
    log.info("Fetching IP from service %r", service.name)
    try:
        data: dict[str, str] = await fetch_api(service.url)
    except aiohttp.ClientError as e:
        log.error("Failed to fetch IP from service %r: %s", service.name, e)
        raise e

    ip_address = data.get(service.field) or ""
    log.info("IP %s fetched from service %r", ip_address, service.name)
    return ip_address


async def fetch_ip_fastest(timeout: float = 1) -> str:

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

    for task in pending:
        log.info("Cancel task: %s", task)
        task.cancel()

    log.info("done tasks: %s", done)

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception %r",
                task.get_name(),
                error,
            )
            continue
        result = task.result()
        log.info("IP %r from service %r", result, task.get_name())
        return result

    log.info("No results fetched.")
    return ""


async def main() -> str:
    configure_logging()
    log.info("Starting 08")

    my_ip = await fetch_ip_fastest(timeout=0.1)
    log.info("my_ip: %s", my_ip)

    log.info("Finished 08")

    return my_ip


if __name__ == "__main__":
    result = asyncio.run(main())
    log.info("final result: %s", result)
