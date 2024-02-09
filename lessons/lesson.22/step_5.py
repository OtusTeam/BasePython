"""
asyncio TaskGroup example
"""

import asyncio
import logging

import common

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    await asyncio.sleep(0.5)
    log.info("Done, got weather")
    return {"weather": {}}


async def get_currencies():
    log.info("Start getting currencies")
    await asyncio.sleep(1)
    log.info("Done, got currencies")
    return {"currencies": [1, 2, 3]}


async def main():
    common.configure_logging()
    log.info("Starting step 5")

    weather_coro = get_weather()

    async with asyncio.TaskGroup() as tg:
        task_weather = tg.create_task(weather_coro, name="get-weather")
        log.info("task weather: %s", task_weather)
        # await asyncio.sleep(1)
        task_currencies = tg.create_task(get_currencies(), name="get-currencies")

    weather_result = task_weather.result()
    currencies_result = task_currencies.result()
    # weather_result, currencies_result = res
    # log.info("Result: %s", res)
    log.info("Weather result: %s", weather_result)
    log.info("Currencies result: %s", currencies_result)
    log.info("Done")


if __name__ == "__main__":
    asyncio.run(main())
