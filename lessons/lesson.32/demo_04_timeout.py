import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather() -> dict:
    log.info("Getting weather data")
    # url = "https://openweathermap.org/?city=Moscow"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    # await asyncio.sleep(1)
    powers = {}
    for i in range(8_000):
        powers[i] = i**i
        await asyncio.sleep(0)

    log.info("len powers: %d", len(powers))

    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies() -> dict:
    log.info("Getting currencies data")
    # url = "https://exchange-rate.org/?from=FOO&to=BAR"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    await asyncio.sleep(1.1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


async def get_weather_and_currencies():
    log.info("fetch started")
    currencies_task = asyncio.create_task(get_currencies())  # 2
    log.info("currencies task: %s", currencies_task)
    # currencies_coro = get_currencies()
    # log.info("currencies task: %s", currencies_coro)

    try:
        async with asyncio.timeout(1):  # 3
            weather, currencies = await asyncio.gather(  # 4
                get_weather(),  # 5
                currencies_task,  # 6
            )
    except TimeoutError:
        log.info("currencies_task done? %s", currencies_task.done())
        log.info("currencies_task cancelled? %s", currencies_task.cancelled())
        raise

    log.info("fetch completed")
    return weather, currencies


async def main() -> None:
    configure_logging()

    log.warning("starting")

    try:
        weather, currencies = await get_weather_and_currencies()  # 1
    except TimeoutError:
        log.exception("could not fetch")
    else:
        log.info("weather result %s", weather)
        log.info("currencies result %s", currencies)

    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
