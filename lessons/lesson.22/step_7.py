import asyncio
import logging
from dataclasses import dataclass

import aiohttp


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


@dataclass
class Service:
    name: str
    url: str
    field: str


SERVICES = [
    Service(name="httpbin-org-ssl", url="https://httpbin.org/get", field="origin"),
    Service(name="httpbin-org", url="http://httpbin.org/get", field="origin"),
    Service(name="ip-api", url="http://ip-api.com/json", field="query"),
    Service(name="ipify", url="https://api.ipify.org/?format=json", field="ip"),
]


async def get_response_data(url: str, field: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            result = data.get(field)
            return result


async def find_ip(time_limit: int | float = 1) -> str:
    tasks = {
        asyncio.create_task(
            get_response_data(url=service.url, field=service.field),
            name=service.name,
        )
        for service in SERVICES
    }

    done, pending = await asyncio.wait(
        tasks,
        timeout=time_limit,
        return_when=asyncio.FIRST_COMPLETED,
    )

    for task in pending:  # type: asyncio.Task
        task.cancel()
        log.info("cancelled task %s", task.get_name())

    result = ""
    for task in done:  # type: asyncio.Task
        result = task.result()
        break
    else:
        log.warning("could not find any data")

    log.debug("result is %s", result)
    return result


async def main():
    log.info("Started searching IP")
    result = await find_ip(time_limit=0.3)
    log.info("result: %s", result)
    log.info("Finished searching IP")
    return result


if __name__ == "__main__":
    ip = asyncio.run(main())
    print("ip", ip)
