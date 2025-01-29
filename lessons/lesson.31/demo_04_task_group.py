import asyncio

import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(1)
    log.info("Got weather")
    return {"weather": {"rain-chance": 50}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1.01)
    log.info("Got currencies")
    return {"currencies": {"exchange-rate": 42}}


async def main() -> None:
    configure_logging()
    log.info("Starting main 04")

    weather_coro = get_weather()
    log.info("created weather coro: %s", weather_coro)

    # weather, currencies

    log.info("Start task group")
    async with asyncio.TaskGroup() as tg:
        task_currencies = tg.create_task(get_currencies())
        log.info("created task for getting currencies: %s", task_currencies)
        task_weather = tg.create_task(weather_coro)
        log.info("created task for getting weather: %s", task_weather)
        log.info("---- all tasks set!")
        log.info("[1] status for weather coro. is done? %s", task_weather.done())
        log.info("do smth else")
        await asyncio.sleep(0)
        # await asyncio.sleep(0.5)
        # tg.create_task(new_call(res))
        # await asyncio.sleep(2)
        log.info("smth else OK DONE")

    log.info("[2] status for weather coro. is done? %s", task_weather.done())
    log.info("++++ task group done")

    weather = task_weather.result()
    currencies = task_currencies.result()
    log.info("weather result: %s", weather)
    log.info("currencies result: %s", currencies)

    log.info("Finished main 04")


if __name__ == "__main__":
    asyncio.run(main())
