import asyncio
# from time import sleep
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # sleep(3)
    d = {}
    # for n in range(7000):
    #     d[n] = n**n
    #     if not n % 100:
    #         await asyncio.sleep(0)
    await asyncio.sleep(1.2)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies():
    log.info("Start getting currencies")
    # 1 / 0
    await asyncio.sleep(1.1)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def get_weather_and_currencies():
    weather_coro = get_weather()
    log.info("created weather coro: %s", weather_coro)

    async with asyncio.timeout(1.15):
        weather, currencies, _ = await asyncio.gather(
            get_currencies(),
            weather_coro,
            get_currencies(),
        )

    log.info("weather result: %s", weather)
    log.info("currencies result: %s", currencies)
    return weather, currencies


async def main() -> None:
    configure_logging()
    log.info("Starting main 05")
    try:
        await get_weather_and_currencies()
    except TimeoutError:
        log.error("Could not fetch weather and currencies due to timeout")
    log.info("Finished main 05")


if __name__ == "__main__":
    asyncio.run(main())
