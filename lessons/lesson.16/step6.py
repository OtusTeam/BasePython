import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('TOKEN_OWM')

city = 'Moscow'

url = 'https://api.openweathermap.org/data/2.5/weather'

params = {
    'q': city,
    'appid': api_key,
    'units': 'metric',
    'lang': 'ru'
}

response = requests.get(url, params=params)

print(response)

if response.status_code == 200:
    print('OK')
    data = response.json()
    print(data)
    temp = data.get('main').get('temp')


    print(f'Температура в {city} - {temp}')
