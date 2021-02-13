# from datetime import datetime
#
# from django.db import models
#
#
# class Location(models.Model):
#     def __init__(self, lon, lat, timezone, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.latitude = lat
#         self.longitude = lon
#         self.timezone = timezone
#
#     latitude = models.IntegerField(null=False, blank=False)
#     longitude = models.IntegerField(null=False, blank=False)
#     timezone = models.CharField(max_length=100, blank=False, null=False)
#
#
# class Weather(models.Model):
#     def __init__(self, json, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         lon = json['coord']['lon'],
#         lat = json['coord']['lat'],
#         timezone = datetime.utcfromtimestamp(json['timezone']).strftime('%H'),
#         self.location = Location(lon, lat, timezone)
#         self.min_temp = json['main']['temp_min'],
#         self.max_temp = json['main']['temp_max'],
#         self.sunrise = datetime.utcfromtimestamp(json['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
#         self.sunset = datetime.utcfromtimestamp(json['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
#
#     location = Location(0, 0, 0)
#     sunset = models.TimeField(null=True)
#     sunrise = models.TimeField(null=True)
#     max_temp = models.IntegerField(null=True)
#     min_temp = models.IntegerField(null=True)
