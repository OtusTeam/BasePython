import asyncio
from dataclasses import dataclass

# from time import sleep
import logging
from random import random, randint

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class WeatherData:
    city: str
    temperature: float
    rain_chance: int


async def fetch_weather_from_api(region_id: int) -> WeatherData | None:
    sleep_time = random()
    log.info(
        "get city-%03d, wait for %.3f seconds",
        region_id,
        sleep_time,
    )
    # send a real HTTP request to API
    await asyncio.sleep(sleep_time)
    # if something happens - there's an error.
    # could not get weather
    if random() < 0.3:
        return

    return WeatherData(
        city=f"City {region_id:03d}",
        temperature=random() * 30,
        rain_chance=randint(0, 100),
    )


async def get_weather(region_id: int) -> WeatherData:
    data = await fetch_weather_from_api(region_id)
    if not data:
        log.warning("Failed to fetch weather data for City %03d", region_id)
        raise ValueError(region_id)

    log.info("got weather for %03d", region_id)
    return data


async def get_regions_weather(*regions_ids: int) -> list[WeatherData]:
    log.info("Request weather for %d regions", len(regions_ids))

    tasks = {
        # create all tasks
        asyncio.create_task(
            # create coro to get weather
            get_weather(region_id=region_id),
            # task name
            name=f"city-{region_id:03d}",
        )
        for region_id in regions_ids
    }

    log.info("Tasks: %s", tasks)

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("Task %r cancelled", task.get_name())

    weathers: list[WeatherData] = []

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        data: WeatherData = task.result()
        weathers.append(data)

    log.info("%d weathers fetched", len(weathers))
    return weathers


async def main() -> None:
    configure_logging()
    log.info("Starting main 06")
    # await get_regions_weather(1, 2, 3)
    weathers = await get_regions_weather(*range(1, 101))
    for weather in weathers:
        print(weather)
    log.info("Finished main 06")


if __name__ == "__main__":
    asyncio.run(main())
