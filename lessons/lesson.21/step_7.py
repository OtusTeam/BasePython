import asyncio
from dataclasses import dataclass
import logging
from aiohttp import ClientSession

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    # Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
    Service(name="httpbin", url="http://httpbin.org/get", field="origin"),
    Service(name="httpbin-ssl", url="https://httpbin.org/get", field="origin"),
]


async def fetch_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def get_from_ip_service(service: Service) -> str:
    log.info("fetch ip from %s", service.name)
    data = await fetch_api(service.url)
    ip_info = data.get(service.field, "")
    log.info("got data from %s: %s", service.name, ip_info)
    return ip_info


async def get_ip(timeout: float = 1) -> str:
    tasks = {
        asyncio.create_task(
            get_from_ip_service(service=service),
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
        log.info("cancelled task %s", task.get_name())

    result = ""
    for task in done:
        result = task.result()
        break
    else:
        log.warning("could not get any data")

    return result


def main():
    configure_logging()

    log.info("Start main")
    ip = asyncio.run(get_ip())
    # result = await get_ip(0.2)
    log.info("got result %s", ip)
    log.info("Finish main")


if __name__ == "__main__":
    main()
