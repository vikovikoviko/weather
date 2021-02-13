from django.shortcuts import render
import requests
import random
from datetime import datetime

from django.urls import reverse
from django.utils.html import format_html


def weather(request):
    cities = ['Gabrovo', 'Sofia', 'Plovdiv', 'Varna']
    cityName = random.choice(cities)
    response = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q=' + cityName + '&appid=c3afb7e24dedb09e3ca373a8cb64747d')
    weatherInLocation = response.json()
    print(response)
    return render(request, 'weather.html', {
        'city': cityName,
        'lon': weatherInLocation['coord']['lon'],
        'lat': weatherInLocation['coord']['lat'],
        'timezone': datetime.utcfromtimestamp(weatherInLocation['timezone']).strftime('%H'),
        'min_temp': weatherInLocation['main']['temp_min'],
        'max_temp': weatherInLocation['main']['temp_max'],
        'sunrise': datetime.utcfromtimestamp(weatherInLocation['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
        'sunset': datetime.utcfromtimestamp(weatherInLocation['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
    })
