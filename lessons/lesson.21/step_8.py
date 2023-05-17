import asyncio
import logging
from dataclasses import dataclass

from aiohttp import ClientSession


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


logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_response_data(url: str, field: str) -> str | None:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            if isinstance(data, dict):
                return data.get(field)


async def find_ip(time_limit: int | float = 1) -> str:
    tasks = {
        asyncio.create_task(
            get_response_data(url=service.url, field=service.field),
            # ОПЦИОНАЛЬНО (имя)
            name=f"task-{service.name}",
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
        log.info("result from %s", task.get_name())
        break
    else:
        log.warning("no done tasks")

    log.info("done with result %r", result)
    return result


def main():
    # result = await get_response_data(url="https://httpbin.org/get", field="origin")
    # result2 = await get_response_data(url="https://jsonplaceholder.typicode.com/todos/1", field="title")
    # log.info("result %s", result)
    # log.info("result2 %s", result2)
    result = asyncio.run(find_ip())
    log.info("result ip %s", result)


if __name__ == "__main__":
    main()
