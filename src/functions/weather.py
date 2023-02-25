from geopy.geocoders import Nominatim
import requests
import json
import logging
from tqdm import trange
from time import sleep
from src.api_keys import OPEN_WEATHER_API_KEY

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")


def weather(weather_init: str):
    weather_return = ''
    try:
        location = get_weather_location(weather_init)
        lon = location.longitude
        lat = location.latitude
        for i in trange(5):
            sleep(.1)

        data = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={OPEN_WEATHER_API_KEY}&units=imperial')
        data_return = json.loads(data.text)

        temp = data_return.get('main')
        wind = data_return.get('wind')
        overcast = data_return.get('weather')

        weather_return += (f"- The weather today is going to be {overcast[0]['description']} \n")
        weather_return += '\n'
        weather_return += (f"- With wind speeds of {wind['speed']} MPH, at {wind['deg']} degrees \n")
        weather_return += '\n'
        weather_return += f"- The temperature today will reach a high of {temp['temp_max']} and a low of {temp['temp_min']}."
        weather_return += f"Currently, the temperature is {temp['temp']} with {temp['humidity']}% humidity\n"
    except Exception as e:
        logging.exception(e)

    return weather_return


def get_weather_location(weather_init: str):
    search_list = ['in', 'for']
    word_split = [word for word in search_list if word in weather_init]

    if word_split:
        user_location = weather_init.split(word_split[0])[1]
        location = "".join(user_location)
    else:
        location = input("Please Enter the city name and state ('Orlando, FL): ")

    detailed_location = geolocator.geocode(location)

    return detailed_location
