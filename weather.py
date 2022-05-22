from re import L
from pyowm.owm import OWM

owm = OWM('4ce782c4b5c4e9519db3771a595cc65b')
lon = 26.1420
lat = 81.7948

mgr = owm.weather_manager()
observation = mgr.weather_at_coords(lon, lat)
w = observation.weather

#print(observation.weather.temperature('fahrenheit'))

def weather():
    temp = w.temperature('fahrenheit')
    wind = w.wind()
    weather_return = ''
    weather_return += (f"- The overcast today is going to be {w.detailed_status} \n")
    weather_return += '\n'
    weather_return += (f"- With wind speeds of {wind['speed']} MPH, at {wind['deg']} degrees with gusts up to {wind['gust']} MPH \n")
    weather_return += '\n'
    weather_return += (f"- The Temperature for today will be {temp['temp']} with the high being {temp['temp_max']} overall it will feel like {temp['feels_like']} \n")

    return  weather_return




