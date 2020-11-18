API_URL = "weather.com"


class WeatherApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    def fetch_weather(self, city: str) -> dict:
        print("got in fetch_weather")
        import requests
        response = requests.get(url=self.base_url, params={"city": city})
        return response.json()


class Weather:
    def __init__(self, api: WeatherApi):
        self.api = api

    def get_temperature(self, city: str) -> int:
        res: dict = self.api.fetch_weather(city=city)
        temperature = res["temperature"]
        return temperature

    def get_humidity(self, city: str) -> float:
        res: dict = self.api.fetch_weather(city=city)
        humidity = res["humidity"]
        return humidity
