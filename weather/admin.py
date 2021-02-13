# import random
# import requests
# from django.contrib import admin
# from django.shortcuts import render
# from datetime import datetime
# from .models import Weather
#
#
# def weather_at_location(request, city_name):
#     response = requests.get(
#         'https://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid=c3afb7e24dedb09e3ca373a8cb64747d')
#     weather_in_location = response.json()
#     weather = Weather(weather_in_location)
#     print(response)
#     return render(request, 'weather.html', {
#         city_name,
#         weather,
#     })
#
#
# class Location(admin.ModelAdmin):
#     pass
