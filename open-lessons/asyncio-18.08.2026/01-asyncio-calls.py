import logging

import asyncio

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    await asyncio.sleep(1)
    log.info("got weather data")
    return {"weather": {"temperature": 18}}


async def get_exchange() -> dict:
    log.info("Getting exchange data")
    await asyncio.sleep(1)
    log.info("got exchange data")
    return {"exchange": {"rate": 2}}


async def main() -> None:
    configure_logging()

    log.info("start")
    weather_coro = get_weather()
    log.info("weather coro: %s", weather_coro)
    exchange = await get_exchange()
    weather = await weather_coro
    log.info("weather: %s", weather)
    log.info("exchange: %s", exchange)
    log.info("end")


if __name__ == "__main__":
    asyncio.run(main())
