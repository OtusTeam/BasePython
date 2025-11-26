import asyncio
import logging
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import aiohttp

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)


# информация по одному сервису


@dataclass
class IpService:
    name: str
    url: str
    field: str


# список из известных ресурсов и как оттуда тянем айпи из ответа. плюс название для красоты

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


async def fetch_api(url: str) -> dict[str, Any]:
    """
    отправить один запрос на API и отдать результат
    """
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            return await resp.json()


async def get_ip_from_service(service: IpService) -> str:
    """
    получить по API ответ и вытащить IP из ответа
    """
    log.info("fetch IP address from service %r", service.name)
    data = await fetch_api(service.url)
    ip_address = data.get(service.field) or ""
    log.info(
        "Fetched IP address %r from service %r",
        ip_address,
        service.name,
    )
    return ip_address


async def fetch_ip_fastest(
    services: list[IpService],
    timeout: float = 1,
) -> str:
    """
    отправить задачи на все API и подождать первого ответившего
    """
    tasks = {
        asyncio.create_task(
            get_ip_from_service(service=service),
            name=f"fetch-ip-from-{service.name}",
        )
        for service in services
    }

    done, pending = await asyncio.wait(
        tasks,
        timeout=timeout,
        return_when=asyncio.FIRST_COMPLETED,
    )

    log.info("done: %d tasks", len(done))
    log.info("pending: %d tasks", len(pending))

    for task in pending:
        log.debug(
            "cancel task %r",
            task.get_name(),
        )
        task.cancel()

    for task in done:
        if error := task.exception():

            log.warning(
                "Task %r failed with exception: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        result = task.result()
        log.info(
            "result %r from task %r",
            result,
            task.get_name(),
        )
        if result:
            return result

    log.warning("No IP result fetched")
    return ""


# получить IP адрес от самого быстрого API


async def main() -> str:
    configure_logging(
        level=logging.DEBUG,
    )
    log.info("Starting")

    my_ip = await fetch_ip_fastest(SERVICES)
    log.info("Fetched IP address %r", my_ip)

    log.info("Finishing")
    return my_ip


if __name__ == "__main__":
    ip = asyncio.run(main())
    log.info("got ip %r", ip)
