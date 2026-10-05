from typing import Literal
from dataclasses import dataclass


class WeatherError(Exception):
    pass


class CityNotFoundError(WeatherError):
    def __init__(self, city: str) -> None:
        self.city = city
        super().__init__(city)


@dataclass(frozen=True)
class WeatherData:
    temperature: int
    rain_chance: int
    conditions: Literal["sunny", "cloudly", "rain"]


weather_data = {
    "Moscow": WeatherData(
        temperature=10,
        rain_chance=90,
        conditions="rain",
    ),
    "Sochi": WeatherData(
        temperature=25,
        rain_chance=3,
        conditions="sunny",
    ),
    "Voronezh": WeatherData(
        temperature=15,
        rain_chance=40,
        conditions="cloudly",
    ),
}


def get_temperature(city: str) -> int:
    weather = weather_data.get(city)
    if weather is None:
        raise CityNotFoundError(city)
    return weather.temperature


def demo_weather():
    moscow_temp = get_temperature("Moscow")
    print("Moscow temp:", moscow_temp)
    try:
        omsk_temp = get_temperature("Omsk")
    except CityNotFoundError as e:
        print("city error:", e.args)
        print("problem city:", e.city)
        raise

    print("Omsk temp:", omsk_temp)


def main():
    demo_weather()


if __name__ == "__main__":
    main()
