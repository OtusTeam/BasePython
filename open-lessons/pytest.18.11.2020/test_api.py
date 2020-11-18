from unittest import mock

import pytest
from api import API_URL, WeatherApi, Weather


def get_prepared_weather_helper():
    api = WeatherApi(API_URL)
    weather = Weather(api=api)
    return weather


@pytest.fixture
def mocked_fetch_weather():
    with mock.patch.object(WeatherApi, 'fetch_weather', autospec=True) as mocked_fetch_weather:
        # print('mocked fetch_weather', WeatherApi.fetch_weather)
        yield mocked_fetch_weather
        # print('teardown api')
        # api.close()
    # print('not mocked fetch_weather', api.fetch_weather)
    # print('done teardown for api')


@pytest.fixture
def weather_api(mocked_fetch_weather):
    api = WeatherApi(API_URL)
    return api


@pytest.fixture
def weather(weather_api):
    weather = Weather(api=weather_api)
    return weather


@pytest.fixture(params=["Moscow", "NYC", "Voronezh"])
def city(request):
    return request.param


class TestWeatherApi:
    def test_fetch_weather(self, weather_api, city):
        res = weather_api.fetch_weather(city=city)
        assert res is not None


class TestWeather:

    def test_get_temperature(self, mocked_fetch_weather, weather, city):
        # weather = get_prepared_weather_helper()
        temperature = 13
        mocked_fetch_weather.return_value = {"temperature": temperature}
        res = weather.get_temperature(city)
        assert isinstance(res, int)
        assert res == temperature
        # weather_api.fetch_weather.assert_called()
        # weather_api.fetch_weather.assert_called_once()
        # call_result = weather_api.fetch_weather.asert_called_once_with(city=city)
        call_result = mocked_fetch_weather.assert_called_once_with(weather.api, city=city)
        assert call_result is None

    def test_get_humidity(self, mocked_fetch_weather, weather, city):
        humidity = 42.5
        mocked_fetch_weather.return_value = {"humidity": humidity}
        res = weather.get_humidity(city)
        assert isinstance(res, float)
        assert res == humidity
        # weather_api.fetch_weather.assert_called()
        # weather_api.fetch_weather.assert_called_once()
        mocked_fetch_weather.assert_called_once_with(weather.api, city=city)
