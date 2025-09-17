import asyncio
import logging
import random
from dataclasses import dataclass
from pathlib import Path

from common import configure_logging


NAME = Path(__file__).stem

log = logging.getLogger(__name__)


class WeatherFetchError(Exception):
    def __init__(self, region_id):
        self.region_id = region_id
        super().__init__(region_id)


@dataclass
class WeatherData:
    region_id: int
    city: str
    temperature: int
    rain_chance: int


async def fetch_weather_from_api(
    region_id: int,
) -> WeatherData | None:
    sleep_time = random.random()
    log.info(
        "fetching weather for city-%03d from API, sleep time %.4f seconds",
        region_id,
        sleep_time,
    )
    # имитация запроса в сеть
    await asyncio.sleep(sleep_time)

    # будто мы получили ошибку от апи / не смогли подключиться / что-то сломалось
    if random.random() < 0.3:
        log.warning(
            "no weather for region city-%03d",
            region_id,
        )
        return None

    # всё же смогли получить ответ от API, пишем об этом лог и возвращаем
    log.info(
        "returning weather for city-%03d",
        region_id,
    )
    return WeatherData(
        region_id=region_id,
        city=f"City {region_id:03d}",
        temperature=random.randint(-20, 40),
        rain_chance=random.randint(0, 100),
    )


async def get_weather(
    region_id: int,
) -> WeatherData:
    # какая-то обертка для взаимодействия с API
    data = await fetch_weather_from_api(region_id)
    if data is None:
        log.error(
            "error getting weather for city-%03d",
            region_id,
        )
        raise WeatherFetchError(region_id)

    log.info(
        "successfully fetched weather for city-%03d",
        region_id,
    )
    return data


async def get_weather_for_many_regions(
    *region_ids: int,
) -> list[WeatherData]:
    log.info("Getting weather for %d regions", len(region_ids))

    tasks = {
        asyncio.create_task(
            get_weather(region_id=region_id),
            name=f"get-weather-{region_id:03d}",
        )
        for region_id in region_ids
    }
    log.info("created %d tasks", len(tasks))

    done, pending = await asyncio.wait(tasks)

    for task in pending:
        task.cancel()

    weathers: list[WeatherData] = []
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

    log.info("Fetched %d weathers", len(weathers))
    return weathers


async def main() -> None:
    configure_logging(
        level=logging.DEBUG,
    )
    log.info("Starting %s", NAME)

    result = await get_weather_for_many_regions(*range(1, 11))
    log.info("got %d weathers", len(result))
    log.debug("All results: %s", result)

    log.info("Finishing %s", NAME)


if __name__ == "__main__":
    asyncio.run(main())
