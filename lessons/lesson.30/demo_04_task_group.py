import asyncio
import logging
from pathlib import Path

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)


async def get_weather():
    log.info("Start getting weather")
    # response = async ... get("https://openweathermap.org/current")
    # data = async get ... response.json()
    # реальный асинхронный запрос во внешний мир
    # получаем примерно такие данные
    await asyncio.sleep(1)
    data = {
        "weather": {
            "sky": "sunny",
            "rain-chance": 10,
        },
    }
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # response = requests.get("https://opencurrenciesmap.org/current")
    # data = response.json()
    # реальный запрос во внешний мир
    # получаем примерно такие данные
    await asyncio.sleep(1)
    data = {
        "currencies": {
            "exchange-rate": 1.5,
        },
    }
    log.info("Got currencies")
    return data


async def main() -> None:
    configure_logging()
    log.info("Starting")

    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        log.info("Started task group")
        get_weather_task = tg.create_task(get_weather())
        log.info("added get weather to tg: %s", get_weather_task)

        log.info("add 0.5s to wait")
        await asyncio.sleep(0.5)

        get_currencies_task = tg.create_task(currencies_coro)
        log.info("added get currencies to tg: %s", get_currencies_task)

        log.info("add more 0.5s to wait")
        await asyncio.sleep(0.5)
        log.info("done waiting for 0.5")

    log.info("DONE task group.")

    weather = get_weather_task.result()
    currencies = get_currencies_task.result()
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
