import os
from dotenv import load_dotenv

load_dotenv()

token_weather = os.getenv('API_WEATHER')

token_omdb = os.getenv('API_OMDB')

