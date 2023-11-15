import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start get weather")
    await asyncio.sleep(1.0001)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start get currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    configure_logging()

    log.info("Start main")
    weather_coro = get_weather()
    res = await asyncio.gather(
        weather_coro,
        get_currencies(),
        # get_weather(),
        # get_currencies(),
    )
    log.info("result: %s", res)
    log.info("Finish main")


if __name__ == "__main__":
    asyncio.run(main())
