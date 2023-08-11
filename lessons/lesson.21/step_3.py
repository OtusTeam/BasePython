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
    return {"weather": {"moscow": {}}}


async def get_currencies():
    log.info("get currencies")
    # wait for currencies
    # TODO: real API call
    await asyncio.sleep(1)
    log.info("done get currencies")
    return {"currencies": [3, 4, 5]}


async def get_calendar():
    await asyncio.sleep(0)
    return {"calendar": [1, 2, 3]}


async def main():
    configure_logging()
    log.info("start main")
    cal = await get_calendar()
    # log.info("calendar %s", cal)
    coro = get_weather()
    weather, currencies = await asyncio.gather(
        coro,
        get_currencies(),
    )
    log.info("weather %s", weather)
    log.info("currencies %s", currencies)
    log.info("finish main")


if __name__ == '__main__':
    asyncio.run(main())
