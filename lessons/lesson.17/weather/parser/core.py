import requests


class Parser:

    def __init__(self, city):
        self.city = city

    def get_forecast(self, get_response=requests.get):
        api_url = 'https://weather23232233.api.com'
        print('MOCK?', requests.get)
        response = requests.get(api_url)
        data = response.json()
        return data
        # print(requests_module)

    @staticmethod
    def parse_weather_data(data):
        # { gradus: "20C 130F", rain: "true", var: "other" }
        gradus = data['gradus']
        c, _ = gradus.split(" ")
        gradus = int(c.replace('C', ""))
        rain = data['rain']
        rain = rain == "true"
        parsed_data = {
            'gradus': gradus,
            'rain': rain,
        }
        return parsed_data
