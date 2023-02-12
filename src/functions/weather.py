from pyowm.owm import OWM
from geopy.geocoders import Nominatim
from src.api_keys import OPEN_WEATHER_API_KEY
import re

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")


def weather(weather_init: str):
    location = get_weather_location(weather_init)

    owm = OWM(OPEN_WEATHER_API_KEY)
    lon = location.longitude
    lat = location.latitude

    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(lon, lat)
    w = observation.weather

    temp = w.temperature()
    wind = w.wind()
    weather_return = ''
    weather_return += (f"- The overcast today is going to be {w.detailed_status} \n")
    weather_return += '\n'
    weather_return += (
        f"- With wind speeds of {wind['speed']} MPH, at {wind['deg']} degrees with gusts up to {wind['gust']} MPH \n")
    weather_return += '\n'
    weather_return += (
        f"- The temperature for today will be {temp['temp']} with the high being {temp['temp_max']} overall it will feel like {temp['feels_like']} \n")

    return weather_return


def get_weather_location(weather_init: str):
    if 'in' in weather_init:
        user_location = weather_init.split('in')[1]
        location = "".join(user_location)
    else:
        location = input("Please Enter the city name and state ('Orlando, FL): ")

    detailed_location = geolocator.geocode(location)

    return detailed_location
