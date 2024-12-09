from unittest import TestCase
from weather.report.core import Report
#
#
# class TestReport:
#
#     def test_create_weather_report(self):
#         report = Report({'gradus': 3, 'rain': True})
#         assert report.create_weather_report() == "Current weather: 3 and rain: yes"

class ReportTestCase(TestCase):

    def test_create_weather_report(self):
        report = Report({'gradus': 3, 'rain': True})
        # assert report.create_weather_report() == "Current weather: 3 and rain: yes"
        self.assertEqual(report.create_weather_report(), "Current weather: 3 and rain: yes")

        with self.assertRaises(Exception):
            raise Exception