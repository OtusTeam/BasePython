import asyncio
import logging
import random
from dataclasses import dataclass

from common import configure_logging

log = logging.getLogger(__name__)


@dataclass
class WeatherData:
    location: str
    temperature: float
    rain_chance: int


async def fetch_weather_from_api(location_id: int) -> WeatherData | None:
    """
    :param location_id: id
    :return: data if success, else None
    """

    sleep_time = random.random()
    log.info(
        "get weather for location %03d, wait for %.3f seconds",
        location_id,
        sleep_time,
    )
    # send API request (imitate)
    await asyncio.sleep(sleep_time)
    if random.random() < 0.3:
        return None

    return WeatherData(
        location=f"Location #{location_id:03d}",
        temperature=round(random.random() * 30, 2),
        rain_chance=random.randint(0, 100),
    )


async def get_weather(location_id: int) -> WeatherData:
    data = await fetch_weather_from_api(location_id)
    if data is None:
        error_text = f"Failed to get weather for region {location_id}"
        raise ValueError(error_text)

    log.info("Got weather for %03d: %s", location_id, data)
    return data


async def get_weather_for_locations(*location_ids: int) -> list[WeatherData]:
    log.info("Got weather for %d locations", len(location_ids))
    tasks = {
        asyncio.create_task(
            get_weather(location_id),
            name=f"get-weather-for-location-{location_id:03d}",
        )
        for location_id in location_ids
    }
    log.info("Waiting for %d tasks: %s", len(tasks), tasks)

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()
        log.info("Cancelled task: %s", task)

    weather_data: list[WeatherData] = []

    for task in done:
        if error := task.exception():
            log.warning(
                "Task %r failed with exception: %r",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        result: WeatherData = task.result()
        log.info(
            "Task %s result: %s",
            task.get_name(),
            result,
        )
        weather_data.append(result)

    log.info("Fetched %d weather data items", len(weather_data))
    return weather_data


async def main():
    configure_logging()

    log.warning("Starting 07")

    # weathers = await get_weather_for_locations(1, 2, 3)
    weathers = await get_weather_for_locations(*range(1, 101))
    log.info("Got %d weathers: %s", len(weathers), weathers)

    log.warning("Finished 07")


if __name__ == "__main__":
    asyncio.run(main())
