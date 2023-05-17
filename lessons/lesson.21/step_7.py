import asyncio
import logging
from aiohttp import ClientSession

logging.basicConfig(
    level=logging.INFO,
    datefmt="%Y-%m-%d %H:%M:%S",
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)-8s - %(message)s",
)
log = logging.getLogger(__name__)


async def get_response_data(url: str):
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def main():
    result = await get_response_data(url="https://httpbin.org/get")
    result2 = await get_response_data(url="https://jsonplaceholder.typicode.com/todos/1")
    log.info("result %s", result)
    log.info("result2 %s", result2)

if __name__ == "__main__":
    asyncio.run(main())
