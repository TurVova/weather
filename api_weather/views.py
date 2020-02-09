from django.http import JsonResponse

from api_weather.models import DataWeather
from api_weather.utils import get_weather


def receive_weather_data(request) -> JsonResponse:
    """
    Create or update weather data
    """
    city = request.GET.get('city', 'Dnipro')
    data = get_weather(city)
    if data:
        default = {
            'current_temp': data['main']['temp'],
            'temp_min': data['main']['temp_min'],
            'temp_max': data['main']['temp_max'],
            'wind_speed': data['wind']['speed'],
            'weather_condition': data['weather'][0]['description']
        }
        DataWeather.objects.update_or_create(
            city=data.get('name'), defaults=default
        )
        response = {'status': 201}
    else:
        response = {'error': 'No weather data available'}
    return JsonResponse(response)


def get_weather_data(request) -> JsonResponse:
    """
    Get weather data from db
    """
    city = request.GET.get('city', 'Dnipro')
    try:
        data = DataWeather.objects.get(city=city)
        print(data)
    except DataWeather.DoesNotExist:
        response = {
            'error': 'No weather data available'
        }
    else:
        response = {
            'currentTemp': data.current_temp,
            'tempMin': data.temp_min,
            'tempMax': data.temp_max,
            'windSpeed': data.wind_speed,
            'weatherCondition': data.weather_condition,
        }
    return JsonResponse(response)
