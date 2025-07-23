import os
from dotenv import load_dotenv


load_dotenv()

TOKEN_OPENWEATHER = os.getenv("TOKEN_WEATHER")

print(TOKEN_OPENWEATHER)