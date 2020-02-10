from rest_framework import generics
from rest_framework.response import Response

from api_weather.models import DataWeather
from api_weather.serializers import DataWeatherSerializer
from api_weather.utils import get_weather


class ReceiveDataWeatherRetrieveAPIView(generics.RetrieveAPIView):
    """Create or update weather data"""

    def retrieve(self, request, *args, **kwargs):
        city = self.request.query_params.get('city', 'Dnipro')
        data = get_weather(city)
        if data:
            DataWeatherSerializer().create(data)
            response = {'status': 201}
        else:
            response = {'error': 'No weather data available'}

        return Response(response)


class GetDataWeatherRetrieveAPIView(generics.RetrieveAPIView):
    """Get weather data from db"""

    def get_queryset(self):
        city = self.request.query_params.get('city', 'Dnipro')

        try:
            data = DataWeather.objects.get(city=city)
        except DataWeather.DoesNotExist:
            data = None

        return data

    def retrieve(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        if queryset:
            response = DataWeatherSerializer(queryset).data
        else:
            response = {
                'error': 'No weather data available'
            }

        return Response(response)
