import asyncio
import logging
import random
from dataclasses import dataclass
from pathlib import Path

from common import configure_logging

NAME = Path(__file__).stem
log = logging.getLogger(NAME)


type RegionId = int


class WeatherFetchError(Exception):
    def __init__(self, region_id: RegionId):
        self.region_id = region_id
        super().__init__(region_id)


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
        "fetching weather for region %03d from API, wait for %.4f",
        region_id,
        sleep_time,
    )
    # тут мы будто ходим в настоящий API и ждём ответа
    await asyncio.sleep(sleep_time)

    if random.random() < 0.3:
        log.warning(
            "No weather info for region %03d",
            region_id,
        )
        return None

    log.info(
        "got weather info for region %03d, return data",
        region_id,
    )
    return WeatherData(
        region_id=region_id,
        city=f"City {region_id:03d}",
        temperature=random.randint(-20, 30),
        rain_chance=random.randint(0, 100),
    )


async def get_weather(
    region_id: RegionId,
) -> WeatherData:
    region_weather_data = await get_weather_from_api(region_id)
    if region_weather_data is None:
        log.error(
            "Failed to fetch weather for %03d",
            region_id,
        )
        raise WeatherFetchError(region_id)

    log.info(
        "Successfully fetched weather for %s",
        region_weather_data.city,
    )
    return region_weather_data


async def get_weather_for_many_regions(
    *regions_ids: RegionId,
) -> list[WeatherData]:
    log.info(
        "Getting weather for %d regions",
        len(regions_ids),
    )
    tasks = {
        asyncio.create_task(
            get_weather(region_id=region_id),
            name=f"get-weather-{region_id:03d}",
        )
        for region_id in regions_ids
    }
    done, pending = await asyncio.wait(tasks)

    for task in pending:
        log.debug("Task %s cancelled", task.get_name())
        task.cancel()

    # weathers = list[WeatherData]()
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
        weathers.append(task.result())

    log.info(
        "Fetched %d weathers",
        len(weathers),
    )
    return weathers


async def main() -> None:
    configure_logging(level=logging.DEBUG)
    log.info("Starting")

    # await get_weather_for_many_regions(1, 2)
    weathers = await get_weather_for_many_regions(*range(1, 11))

    log.info(
        "Fetched weathers for %d regions: %s",
        len(weathers),
        weathers,
    )

    log.info("Finishing")


if __name__ == "__main__":
    asyncio.run(main())
