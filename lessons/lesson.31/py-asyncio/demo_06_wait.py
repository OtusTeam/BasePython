import asyncio
import logging
from dataclasses import dataclass
from random import random, randint

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class WeatherData:
    city: str
    temperature: float
    rain_chance: int


async def fetch_weather_from_api(
    region_id: int,
) -> WeatherData | None:
    sleep_time = random()
    log.info(
        "get city-%03d, wait for %.3f seconds",
        region_id,
        sleep_time,
    )
    # как бы отправляем реальный HTTP запрос в сеть
    await asyncio.sleep(sleep_time)
    # что-то пошло не так с запросом, он отвалился - выкидываем исключение
    if random() < 0.3:
        return None

    return WeatherData(
        city=f"City {region_id:03d}",
        temperature=random() * 30,
        rain_chance=randint(0, 100),
    )


async def get_weather(region_id: int) -> WeatherData:
    data = await fetch_weather_from_api(region_id)

    if not data:
        log.warning("Failed to get weather for region %03d", region_id)
        raise ValueError(region_id)

    log.info("got weather for %03d", region_id)
    return data


async def get_weather_for_many_regions(
    *regions_ids: int,
) -> list[WeatherData]:
    log.info("Get weather data for %d regions", len(regions_ids))

    tasks = {
        asyncio.create_task(
            get_weather(region_id),
            name=f"get-weather-{region_id:03d}",
        )
        for region_id in regions_ids
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()

    weathers = []
    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        weathers.append(task.result())

    log.info("Got weather for %d regions", len(weathers))
    return weathers


async def main() -> None:
    configure_logging()
    log.info("Starting 06")

    # weathers = await get_weather_for_many_regions(42, 11, 35)
    weathers = await get_weather_for_many_regions(*range(100))
    log.info("Got weathers: %s", weathers)
    log.info("Finished 06")


if __name__ == "__main__":
    asyncio.run(main())
