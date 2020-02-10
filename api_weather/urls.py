from django.urls import path

from api_weather import views

urlpatterns = [
    path('syncWeather/', views.ReceiveDataWeatherRetrieveAPIView.as_view()),
    path('currentWeather/', views.GetDataWeatherRetrieveAPIView.as_view()),
]
