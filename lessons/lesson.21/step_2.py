import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("get weather")
    # wait for weather
    # TODO: real API call
    await asyncio.sleep(1)
    log.info("done get weather")


async def get_currencies():
    log.info("get currencies")
    # wait for currencies
    # TODO: real API call
    await asyncio.sleep(1)
    log.info("done get currencies")


async def main():
    configure_logging()
    log.info("start main")
    coro = get_weather()
    log.info("coro get weather %s", coro)
    await coro
    await get_currencies()
    log.info("finish main")


if __name__ == '__main__':
    asyncio.run(main())
