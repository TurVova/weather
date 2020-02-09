from django.urls import path

from api_weather import views


urlpatterns = [
    path('syncWeather/', views.receive_weather_data),
    path('currentWeather/', views.get_weather_data),
]
