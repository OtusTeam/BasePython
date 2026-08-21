import logging

import asyncio

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    # response = await httpx.get("https://www.openweathermap.org/query=Moscow")
    await asyncio.sleep(1)
    log.info("got weather data")
    return {"weather": {"temperature": 18}}


async def get_exchange() -> dict:
    log.info("Getting exchange data")
    # response = await httpx.get("https://www.openexchangemap.org/query=Moscow")
    await asyncio.sleep(1.0001)
    log.info("got exchange data")
    return {"exchange": {"rate": 2}}


async def main() -> None:
    configure_logging()

    log.info("start")
    weather_coro = get_weather()
    log.info("weather coro: %s", weather_coro)

    exchange, weather = await asyncio.gather(
        get_exchange(),
        weather_coro,
    )

    log.info("weather: %s", weather)
    log.info("exchange: %s", exchange)
    log.info("end")


if __name__ == "__main__":
    asyncio.run(main())
