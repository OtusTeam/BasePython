import asyncio
import logging

from logging_config import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # response = requests.get("https://httpbin.org/get")
    # response = requests.get("https://openweathermap.org/json")
    # data = response.json()
    # тут мы имитируем отправку запроса во внешний мир.
    # нас интересует только время ожидания.
    # await asyncio.sleep(1.001)
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
    # response = requests.get("https://httpbin.org/get-exchange-rate")
    # response = requests.get("https://opencurrenciesmap.org/json")
    # data = response.json()
    # тут мы имитируем отправку запроса во внешний мир.
    # нас интересует только время ожидания.
    await asyncio.sleep(1)
    data = {
        "currencies": {
            "exchange-rate": 1.5,
        },
    }
    log.info("Got currencies")
    return data


async def main():
    configure_logging()
    log.info("Starting")
    currencies_coro = get_currencies()
    log.info("currencies coro: %s", currencies_coro)

    async with asyncio.TaskGroup() as tg:
        log.info("Task Group started")
        get_weather_task = tg.create_task(get_weather())
        log.info("created task for get_weather: %s", get_weather_task)

        log.info("wait 0.5s before proceeding")
        await asyncio.sleep(0.5)

        get_currencies_task = tg.create_task(currencies_coro)
        log.info("created task for currencies_coro: %s", get_currencies_task)

        # log.info("wait more 0.5s before proceeding")
        # await asyncio.sleep(0.5)
        log.info("wait more 0.4s before proceeding")
        await asyncio.sleep(0.4)
        log.info("Last line inside task group")
    log.info("DONE Task Group")

    log.info("get_weather task after tg: %s", get_weather_task)
    log.info("get_currencies task after tg: %s", get_currencies_task)

    weather = get_weather_task.result()
    currencies = get_currencies_task.result()
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)
    log.info("Finished")


if __name__ == "__main__":
    asyncio.run(main())
