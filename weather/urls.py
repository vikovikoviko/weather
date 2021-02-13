from django.urls import path
from weather import views
from weather import admin

urlpatterns = [
    path('', views.weather, name='weather'),
]
