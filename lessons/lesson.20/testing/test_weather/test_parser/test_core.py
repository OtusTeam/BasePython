from unittest import TestCase
from weather.parser.core import Parser


class MockResponse:

    def json(self, *args, **kwargs):
        return {
            'gradus': "20C 130F",
            'rain': "true",
            'other': "other"
        }


def mock_get(url, *args, **kwargs):
    return MockResponse()


class ParserTestCase(TestCase):

    def setUp(self):
        print('Я выполняюсь перед каждым тестом')
        self.data = {
            'gradus': "20C 130F",
            'rain': "true",
            'other': "other"
        }

    def test_parse_weather_data(self):
        result = Parser.parse_weather_data(self.data)
        expected = {
            'gradus': 20,
            'rain': True
        }
        self.assertEqual(result, expected)

    # def test_get_forecast(self):
    #     parser = Parser('Москва')
    #     result = parser.get_forecast(mock_get)
    #     expected = {
    #         'gradus': "20C 130F",
    #         'rain': "true",
    #         'other': "other"
    #     }
    #     self.assertEqual(result, expected)

    def tearDown(self):
        print('Я выполняюсь после каждого метода')

    def test_sum(self):
        self.assertEqual(1 + 2, 3)
