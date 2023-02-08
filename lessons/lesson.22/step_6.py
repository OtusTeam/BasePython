import asyncio
import logging

import aiohttp


logging.basicConfig(
    format="[%(asctime)s.%(msecs)03d] %(module)s:%(lineno)d %(levelname)s - %(message)s",
    level=logging.DEBUG,
    datefmt="%Y-%m-%d %H:%M:%S",
)

log = logging.getLogger(__name__)


async def get_response_data(url: str, field: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            result = data.get(field)
            return result


async def main():
    result = await get_response_data("https://httpbin.org/get", "origin")
    log.info("result: %s", result)


if __name__ == "__main__":
    asyncio.run(main())
