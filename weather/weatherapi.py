import requests

from weather.models import Weather, Location


def get_weather(city):
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q='
        + city + '&appid=c3afb7e24dedb09e3ca373a8cb64747d')
    json = response.json()
    weather = Weather()
    location = Location()
    weather.city_name = city
    location.longitude = json['coord']['lon']
    location.latitude = json['coord']['lat']
    location.timezone = json['timezone']
    weather.sunset = json['sys']['sunset']
    weather.sunrise = json['sys']['sunrise']
    weather.max_temp = json['main']['temp_max']
    weather.min_temp = json['main']['temp_min']
    weather.location = location
    return weather


def get_cities():
    return ['varna', 'gabrovo', 'sofia', 'plovdiv']
