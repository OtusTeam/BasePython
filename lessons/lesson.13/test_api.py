from unittest import mock

from api import get_weather, get_temp, API_URL


@mock.patch("api.fetch")
def test_get_weather(mocked_fetch):
    city = "Moscow"
    res = get_weather(city)
    assert res is mocked_fetch.return_value
    mocked_fetch.assert_called_once_with(API_URL, {"city": city})


@mock.patch("api.fetch")
def test_get_temp(mocked_fetch):
    temp = 42
    city = "qwerty"
    mocked_fetch.return_value = {"temp": temp}
    res = get_temp(city)
    assert res == temp
    mocked_fetch.assert_called_once_with(API_URL, {"city": city})
