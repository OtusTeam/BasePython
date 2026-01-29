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
    weather = await get_weather()
    log.info("Weather result: %s", weather)
    currencies = await currencies_coro
    log.info("Currencies result: %s", currencies)
    log.info("Finished")


async def run_currencies_and_validate(coro):
    res = await coro
    validate(res)
    return res


async def example():
    currencies_coro = get_currencies()
    res = await run_currencies_and_validate(currencies_coro)


if __name__ == "__main__":
    asyncio.run(main())
