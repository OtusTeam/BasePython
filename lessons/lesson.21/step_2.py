import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start get weather")
    await asyncio.sleep(2)
    log.info("Done, got weather")


async def get_currencies():
    log.info("Start get currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return 42


async def main():
    configure_logging()

    log.info("Start main")
    weather_coro = get_weather()
    log.info("get_weather: %s", weather_coro)
    await weather_coro
    log.info("get_currencies: %s", await get_currencies())
    log.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
