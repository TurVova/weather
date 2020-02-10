from rest_framework import serializers
from api_weather.models import DataWeather


class DataWeatherSerializer(serializers.ModelSerializer):
    """Serializer for DataWeather model"""

    class Meta:
        model = DataWeather
        exclude = ['id']

    def create(self, validated_data: dict) -> bool:
        defaults = {
            'current_temp': validated_data['main']['temp'],
            'temp_min': validated_data['main']['temp_min'],
            'temp_max': validated_data['main']['temp_max'],
            'wind_speed': validated_data['wind']['speed'],
            'weather_condition': validated_data['weather'][0]['description']
        }
        DataWeather.objects.update_or_create(
            city=validated_data.get('name'), defaults=defaults
        )
        return True
