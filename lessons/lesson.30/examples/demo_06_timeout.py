import asyncio
import logging
from contextlib import suppress

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Start getting weather")
    # await fetch_slow_api()
    await asyncio.sleep(1.5)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_weather_time_limited_or_none(timeout: float = 1.5) -> dict | None:
    # try:
    #     async with asyncio.timeout(timeout):
    #         return await get_weather()
    # except TimeoutError:
    #     return None
    with suppress(TimeoutError):
        async with asyncio.timeout(timeout):
            return await get_weather()

    return None


async def get_currencies() -> dict:
    log.info("Start getting currencies")
    # await fetch_slow_api()
    await asyncio.sleep(1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def get_weather_and_currencies():

    currencies_coro = get_currencies()
    log.info("get currencies coro: %s", currencies_coro)

    async with asyncio.timeout(1.5):
        # async with asyncio.TaskGroup() as tg:
        #     tg.create_task(get_weather())
        #     tg.create_task(currencies_coro)
        weather, currencies = await asyncio.gather(
            # get_weather(),
            get_weather_time_limited_or_none(1),
            currencies_coro,
        )
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    return weather, currencies


async def async_main() -> None:
    log.info("Start main 06 gather with timeout")
    try:
        await get_weather_and_currencies()
    except TimeoutError:
        log.error("Can't get weather and currencies in fixed time")
    log.info("Finished main 06 gather with timeout")


def main() -> None:
    configure_logging()
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
