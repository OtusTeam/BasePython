import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


tasks = set()


async def get_weather() -> dict:
    log.info("Getting weather data")
    # url = "https://openweathermap.org/?city=Moscow"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    # await asyncio.sleep(1.0001)
    await asyncio.sleep(0.5)
    1 / 0
    log.info("fetched weather data")
    return {"weather": {"temperature": 23}}


async def get_currencies() -> dict:
    log.info("Getting currencies data")
    # url = "https://exchange-rate.org/?from=FOO&to=BAR"
    # response = await httpx.get(url)
    # data = response.json()
    # return data
    await asyncio.sleep(1)
    log.info("fetched currencies data")
    return {"currencies": {"rate": 42}}


async def get_weather_and_currencies():
    log.info("fetch started")

    currencies_task = asyncio.create_task(get_currencies())
    tasks.add(currencies_task)
    log.info("currencies task: %s", currencies_task)

    try:
        weather, currencies = await asyncio.gather(
            get_weather(),
            currencies_task,
        )
    except ZeroDivisionError:
        log.error("could not fetch")
        log.info("currencies_task: %s", currencies_task)
        log.info("currencies_task done? %s", currencies_task.done())
        log.info("currencies_task cancelled? %s", currencies_task.cancelled())
        return None, None
    log.info("fetch completed")
    return weather, currencies


async def main() -> None:
    configure_logging()

    log.warning("starting")

    weather, currencies = await get_weather_and_currencies()

    log.info("weather result %s", weather)
    log.info("currencies result %s", currencies)

    log.info("tasks before finishing: %s", tasks)
    # for task in tasks:
    #     log.info("waiting for task %s", task)
    #     log.info("result: %s", await task)
    log.warning("finishing...")
    await asyncio.sleep(1)
    log.warning("now done.")


if __name__ == "__main__":
    asyncio.run(main())
