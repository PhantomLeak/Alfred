from re import L
from pyowm.owm import OWM

owm = OWM('4ce782c4b5c4e9519db3771a595cc65b')
naples_lon = 26.1420
naples_lat = 81.7948

mgr = owm.weather_manager()
observation = mgr.weather_at_coords(naples_lat, naples_lon)
w = observation.weather

print(f"The overcast todya is going to be {w.detailed_status}")
print(w.wind())
print(w.temperature())

#forecast = mgr.forecast_at_coords(naples_lat,naples_lon,'5h')




