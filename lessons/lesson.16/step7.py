import requests
import os
from dotenv import load_dotenv


load_dotenv()
api_key = os.getenv('TOKEN_OMDB')



url = 'http://www.omdbapi.com/'

movie = 'Matrix'


params = {
    't': movie,
    'apikey': api_key,

}

response = requests.get(url, params=params)

print(response)

if response.status_code == 200:
    print('OK')
    data = response.json()
    print(data)
    # temp = data.get('main').get('temp')


    # print(f'Температура в {city} - {temp}')
