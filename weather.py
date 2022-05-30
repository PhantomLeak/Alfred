from re import L
from pyowm.owm import OWM
from geopy.geocoders import Nominatim

# Initialize Nominatim API
geolocator = Nominatim(user_agent="MyApp")

def weather():
    get_location = input("Please Enter the city name and state ('Orlando, FL): ")
    location = geolocator.geocode(get_location)

    owm = OWM('4ce782c4b5c4e9519db3771a595cc65b')
    lon = location.longitude
    lat = location.latitude

    mgr = owm.weather_manager()
    observation = mgr.weather_at_coords(lon, lat)
    w = observation.weather

    # print(observation.weather.temperature('fahrenheit'))

    temp = w.temperature('fahrenheit')
    wind = w.wind()
    weather_return = ''
    weather_return += (f"- The overcast today is going to be {w.detailed_status} \n")
    weather_return += '\n'
    weather_return += (f"- With wind speeds of {wind['speed']} MPH, at {wind['deg']} degrees with gusts up to {wind['gust']} MPH \n")
    weather_return += '\n'
    weather_return += (f"- The Temperature for today will be {temp['temp']} with the high being {temp['temp_max']} overall it will feel like {temp['feels_like']} \n")

    return  weather_return