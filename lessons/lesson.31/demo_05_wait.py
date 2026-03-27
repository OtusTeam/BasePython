import asyncio
import logging
import random
from dataclasses import dataclass

from common import configure_logging

log = logging.getLogger(__name__)

type RegionId = int


class WeatherFetchError(Exception):
    def __init__(self, region_id: RegionId):
        self.region_id = region_id
        super().__init__(region_id)


@dataclass
class WeatherData:
    region_id: RegionId
    temperature: int


async def get_weather_from_api(
    region_id: RegionId,
) -> WeatherData | None:
    sleep_time = random.random()
    log.info(
        "Fetching weather data from API for region %s, sleep %.4f",
        region_id,
        sleep_time,
    )
    await asyncio.sleep(sleep_time)
    if random.random() < 0.3:
        log.warning(
            "No weather for region %s",
            region_id,
        )
        return None

    return WeatherData(
        region_id=region_id,
        temperature=random.randint(-20, 40),
    )


async def get_weather(
    region_id: RegionId,
) -> WeatherData:
    log.debug(
        "Get weather from api for region %s",
        region_id,
    )
    data = await get_weather_from_api(region_id)
    if data is None:
        log.error(
            "Failed to get weather data for region %s",
            region_id,
        )
        raise WeatherFetchError(region_id=region_id)

    log.info(
        "Successfully got weather data for region %s, data: %s",
        region_id,
        data,
    )
    return data


async def get_weather_for_many_regions(
    *regions_ids: RegionId,
) -> list[WeatherData]:
    if not regions_ids:
        log.warning("No regions to get weather data for")
        return []

    tasks = {
        asyncio.create_task(
            get_weather(region_id),
            name=f"get-weather-for-{region_id}",
        )
        for region_id in regions_ids
    }
    log.info("Start %d tasks", len(tasks))

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
                "Task %s failed for region: %s",
                task.get_name(),
                error,
                # exc_info=error,
            )
            continue
        weathers.append(task.result())

    return weathers


async def main():
    configure_logging()
    log.info("Starting")

    weathers = await get_weather_for_many_regions(*range(1, 201))

    log.info(
        "Got %d weather results",
        len(weathers),
    )

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
