class Report:

    def __init__(self, data):
        # { gradus: 20, rain: true }
        self.data = data

    def create_weather_report(self):
        weather = self.data['gradus']
        is_rain = self.data['rain']
        rain_text = 'yes' if is_rain else 'no'
        return f"Current weather: {weather} and rain: {rain_text}"
