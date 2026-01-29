import asyncio
import logging
import random
from dataclasses import dataclass

from logging_config import configure_logging

log = logging.getLogger(__name__)

type RegionId = int


class WeatherFetchError(Exception):
    def __init__(self, region_id: RegionId):
        super().__init__(region_id)
        self.region_id = region_id


@dataclass
class WeatherData:
    region_id: RegionId
    city: str
    temperature: int
    rain_chance: int


async def get_weather_from_api(
    region_id: RegionId,
) -> WeatherData | None:
    sleep_time = random.random()
    log.info(
        "Fetching weather for region %03d, sleep for %.4fs",
        region_id,
        sleep_time,
    )
    await asyncio.sleep(sleep_time)
    if random.random() < 0.3:
        log.warning(
            "No weather for region_id: %s",
            region_id,
        )
        return None

    log.info(
        "got weather for region_id: %s",
        region_id,
    )
    return WeatherData(
        region_id=region_id,
        city=f"City {region_id:03d}",
        temperature=random.randint(-10, 20),
        rain_chance=random.randint(5, 95),
    )


async def get_weather(
    region_id: RegionId,
) -> WeatherData:
    log.debug(
        "Start getting weather for region id: %s",
        region_id,
    )

    data = await get_weather_from_api(region_id)
    if data is None:
        log.error(
            "Failed to get weather for region id: %s",
            region_id,
        )
        raise WeatherFetchError(region_id)

    log.info(
        "Successfully fetched weather for %s",
        data.city,
    )
    return data


async def get_weather_for_many_regions(
    *region_ids: RegionId,
) -> list[WeatherData]:
    if not region_ids:
        log.warning("no regions provided")
        return []

    log.info(
        "getting weather for %d regions",
        len(region_ids),
    )
    tasks = {
        asyncio.create_task(
            get_weather(region_id),
            name=f"get-weather-for-{region_id}",
        )
        for region_id in region_ids
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        log.info(
            "cancelling task %s",
            task.get_name(),
        )
        task.cancel()

    weathers: list[WeatherData] = []
    for task in done:
        if error := task.exception():
            log.error(
                "Task %s failed: %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue

        weathers.append(task.result())

    return weathers


async def main():
    configure_logging(level=logging.DEBUG)
    log.info("Starting")

    # weathers = await get_weather_for_many_regions(1, 2)
    # weathers = await get_weather_for_many_regions(*range(1, 240, 3))
    weathers = await get_weather_for_many_regions(*range(1, 33))
    log.info(
        "Got weather results for %d regions: %s",
        len(weathers),
        weathers,
    )

    log.info("Finished")


if __name__ == "__main__":
    asyncio.run(main())
