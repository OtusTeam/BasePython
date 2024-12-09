from .parser import Parser
from .report import Report

class Weather:

    def __init__(self, city):
        self.city = city

    def create_forecast(self):
        parser = Parser(self.city)
        data = parser.get_forecast()
        parsed_data = Parser.parse_weather_data(data)
        report = Report(parsed_data)
        return report.create_weather_report()