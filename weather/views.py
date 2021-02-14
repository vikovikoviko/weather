from django.shortcuts import render
from datetime import datetime
from weather.weatherapi import get_weather, get_cities


def weather(request):
    cities = list(map(get_weather, get_cities()))
    context = {
        'cities': cities,
    }
    return render(request, 'weather.html', context)
