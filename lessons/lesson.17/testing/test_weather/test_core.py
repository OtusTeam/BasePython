from unittest import TestCase, mock
from weather import Weather
import requests


class MockResponse:

    def json(self, *args, **kwargs):
        return {
            'gradus': "20C 130F",
            'rain': "true",
            'other': "other"
        }


def mock_get(*args, **kwargs):
    return MockResponse()


class WeatherTestCase(TestCase):

    @mock.patch('requests.get', side_effect=mock_get)
    def test_create_forecast(self, mock):
        weather = Weather('Москва')

        # requests.get = mock_get

        result = weather.create_forecast()

        self.assertEqual(len(mock.call_args_list), 1)


        expected = "Current weather: 20 and rain: yes"
        self.assertEqual(expected, result)
