import asyncio
import logging
import random
from dataclasses import dataclass
from itertools import takewhile
from typing import Any, TypedDict

from common import configure_logging


log = logging.getLogger(__name__)


type RegionId = int


class WeatherApiResponseBody(TypedDict):
    temperature: int


@dataclass(slots=True, frozen=True)
class WeatherData:
    region_id: RegionId
    name: str
    temperature: int


class WeatherFetchError(Exception):
    region_id: int

    def __init__(self, region_id):
        self.region_id = region_id
        super().__init__(region_id)


async def get_weather_from_api(
    region_id: RegionId,
) -> WeatherApiResponseBody | None:
    sleep_time = random.random()
    log.info(
        "fetching region %03d, sleep %.4f",
        region_id,
        sleep_time,
    )
    await asyncio.sleep(sleep_time)

    if random.random() < 0.3:
        log.warning(
            "No data from API for region = %03d",
            region_id,
        )
        return None

    return WeatherApiResponseBody(
        temperature=random.randint(-20, 30),
    )


async def get_weather(
    region_id: RegionId,
) -> WeatherData:
    log.info(
        "get weather for region %03d",
        region_id,
    )
    response = await get_weather_from_api(region_id)
    if response is None:
        raise WeatherFetchError(region_id)

    temp = response["temperature"]
    log.info(
        "temp = %02d for region %03d",
        temp,
        region_id,
    )
    return WeatherData(
        region_id=region_id,
        name=f"City-{region_id:03d}",
        temperature=temp,
    )


async def get_weather_for_many_regions(
    *regions_ids: RegionId,
) -> list[WeatherData]:
    if not regions_ids:
        log.warning("No regions provided")
        return []

    tasks = {
        asyncio.create_task(
            get_weather(region_id),
            name=f"task-get_weather({region_id:03d})",
        )
        for region_id in regions_ids
    }
    log.info("starting %d tasks", len(tasks))

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        log.info(
            "cancelling pending task %r",
            task.get_name(),
        )
        task.cancel()

    result_weathers = []
    for task in done:
        if error := task.exception():
            log.debug(
                "skipping exception for region_id = %d, task %r",
                getattr(error, "region_id", -1),
                task.get_name(),
                # exc_info=error,
            )
            continue
        result_weathers.append(task.result())

    return result_weathers


async def main() -> None:
    configure_logging()
    log.warning("starting")
    result = await get_weather_for_many_regions(*range(1, 101))
    log.info("weathers results count = %d", len(result))
    # print(result)

    log.warning("finishing")


if __name__ == "__main__":
    asyncio.run(main())
