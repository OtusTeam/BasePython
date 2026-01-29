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
    await asyncio.sleep(1.5)
    data = {
        "weather": {
            "sky": "sunny",
            "rain-chance": 10,
        },
    }
    log.info("Got weather")
    # 1 / 0
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
    weather, currencies = await asyncio.gather(
        get_weather(),
        currencies_coro,
    )
    log.info("Weather result: %s", weather)
    log.info("Currencies result: %s", currencies)
    log.info("Finished")


if __name__ == "__main__":
    asyncio.run(main())
