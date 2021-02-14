from datetime import datetime

from django.db import models


class Location(models.Model):
    latitude = models.IntegerField(null=False)
    longitude = models.IntegerField(null=False)
    timezone = models.CharField(max_length=100, null=False)

    def get_timezone(self):
        return datetime.utcfromtimestamp(self.timezone).strftime("%H")


class Weather(models.Model):
    city_name = models.CharField(max_length=30, default="")
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True)
    sunset = models.TimeField(null=True)
    sunrise = models.TimeField(null=True)
    max_temp = models.IntegerField(null=True)
    min_temp = models.IntegerField(null=True)

    def get_sunset(self):
        return datetime.utcfromtimestamp(self.sunset).strftime("%H:%M:%S")

    def get_sunrise(self):
        return datetime.utcfromtimestamp(self.sunrise).strftime("%H:%M:%S")
