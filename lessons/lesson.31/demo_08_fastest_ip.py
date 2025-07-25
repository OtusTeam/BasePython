import asyncio

import logging
from collections.abc import Iterable
from dataclasses import dataclass
from pathlib import Path

import aiohttp

from common import configure_logging

NAME = Path(__file__).stem

log = logging.getLogger(__name__)

HTTPBIN_GET = "https://httpbin.org/get"
HTTPBIN_UUID = "https://httpbin.org/uuid"


@dataclass
class IpInfoService:
    name: str
    url: str
    field: str


SERVICES = [
    IpInfoService(
        name="httpbin-http",
        url="http://httpbin.org/get",
        field="origin",
    ),
    IpInfoService(
        name="httpbin-https",
        url="https://httpbin.org/get",
        field="origin",
    ),
    IpInfoService(
        name="pie.dev",
        url="https://pie.dev/get",
        field="origin",
    ),
    IpInfoService(
        name="ip-api",
        url="http://ip-api.com/json",
        field="query",
    ),
    IpInfoService(
        name="ipify",
        url="https://api.ipify.org/?format=json",
        field="ip",
    ),
]


async def fetch_api(
    url: str,
):
    log.info("Fetching %s", url)
    async with (
        aiohttp.ClientSession() as session,
        session.get(url) as response,
    ):
        result = await response.json()

    log.info(
        "got result from %s: %s",
        url,
        result,
    )
    return result


async def fetch_ip_from_service(
    service: IpInfoService,
) -> str:
    log.info(
        "Fetching IP from service: %s",
        service.name,
    )
    try:
        data: dict[str, str] = await fetch_api(service.url)
    except aiohttp.ClientError as e:
        log.error(
            "Failed to fetch IP from service %s: %s",
            service.name,
            e,
        )
        raise e

    ip_address = data.get(service.field) or ""
    log.info(
        "IP %r fetched from service %s",
        ip_address,
        service.name,
    )
    return ip_address


async def fetch_ip_fastest(
    services: Iterable[IpInfoService],
    timeout: float = 1,
) -> str:
    tasks = {
        asyncio.create_task(
            fetch_ip_from_service(
                service=service,
            ),
            name=f"ip-service-{service.name}",
        )
        for service in services
    }

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )
    for task in pending:
        log.debug("Cancelling task: %s", task)
        task.cancel()

    log.info("done %d tasks", len(done))
    log.debug("tasks done: %s", done)

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception %r",
                task.get_name(),
                error,
                exc_info=error,
            )
            continue
        result = task.result()
        log.info(
            "IP %r from %s",
            result,
            task.get_name(),
        )
        return result

    log.warning("No results fetched")
    return ""


async def main():
    configure_logging(
        level=logging.DEBUG,
    )
    log.info("Starting %s", NAME)

    ip_res = await fetch_ip_fastest(SERVICES, timeout=1.5)
    log.info("final result: %r", ip_res)

    log.info("Finishing %s", NAME)

    return ip_res


if __name__ == "__main__":
    ip_result = asyncio.run(main())
    print("got ip result:", ip_result)
