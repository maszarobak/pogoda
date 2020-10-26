from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
city = input('Wpisz miasto: ')
owm = OWM('55ab3b72ce60553c9d1a2cd9208b4e0e')
mgr = owm.weather_manager()

observation = mgr.weather_at_place(city)
w = observation.weather

temperature = w.temperature('celsius')['temp']

print("W " + city + " temperatura wynosi: " + str(temperature) + " celsiusza")
