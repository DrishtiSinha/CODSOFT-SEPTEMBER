import requests
from pprint import pprint
API_Key = '0c0ad12ad02f8a99e0f911884f2cf720'

print = ('1 for city \n2 for lat_long')
choice = int(input('Enter your choice'))

if choice == 1:
     city = input('Enter city name')
     base_url = "https://api.openweathermap.org/data/2.5/weather?appid="+API_Key+"&q="+ city    
     weather_data = requests.get(base_url).json()

elif choice == 2:
    Latitude = float(input('Enter Latitude'))
    Longitude = float(input('Enter Longitude'))
    base_url = "https://api.openweathermap.org/data/2.5/weather?lat="+ Latitude + "&lon" + Longitude + "&appid" +API_Key
    weather_data = requests.get(base_url).json()

else:
    print('dont know')
pprint(weather_data)

