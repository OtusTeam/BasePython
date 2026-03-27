import asyncio
import logging

from common import configure_logging

log = logging.getLogger(__name__)


async def get_weather():
    log.info("Start getting weather")
    # response = requests.get("https://api.openweathermap.org/data/2.5/weather?")
    # data = response.json()
    # нам нужен синтетический пример.
    # Мы не хотим зависеть от внешнего API,
    # мы хотим предсказуемое время ожидания.
    # await asyncio.sleep(2)
    # await asyncio.sleep(1.001)
    # await asyncio.sleep(0)

    d = {}
    for i in range(9_000):
        d[i] = i**i
        # if not i % 10:
        # await asyncio.sleep(0)

    log.info("Processed d size = %d", len(d))

    data = {
        "weather": {
            "sky": "cloudy",
            "temp": "5",
        },
    }
    log.info("Got weather")
    return data


async def get_currencies():
    log.info("Start getting currencies")
    # response = requests.get("https://api.opencurrencies.org/data/2.5/currencies?")
    # data = response.json()
    # нам нужен синтетический пример.
    # Мы не хотим зависеть от внешнего API,
    # мы хотим предсказуемое время ожидания.
    await asyncio.sleep(1)
    # await asyncio.sleep(0)
    data = {
        "currencies": {
            "exchange-rate": 2,
        },
    }
    log.info("Got currencies")
    return data


async def get_weather_and_currencies(
    timeout: float = 1.01,
):
    log.info("Start getting weather and currencies")
    async with asyncio.timeout(timeout):
        weather, currencies = await asyncio.gather(
            get_weather(),
            get_currencies(),
        )

    log.info("weather result: %s", weather)
    log.info("currencies result: %s", currencies)
    return weather, currencies


async def main():
    configure_logging()
    log.info("Starting")

    try:
        weather, currencies = await get_weather_and_currencies()
    except TimeoutError:
        log.error("Timeout error while getting weather and currencies")
    else:
        log.info(
            "Results: weather=%s, currencies=%s",
            weather,
            currencies,
        )

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
