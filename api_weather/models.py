from django.db import models


class DataWeather(models.Model):
    """
    Model for data from openweathermap
    """
    city = models.CharField(max_length=100, unique=True)
    current_temp = models.FloatField(null=True, blank=True)
    temp_min = models.FloatField(null=True, blank=True)
    temp_max = models.FloatField(null=True, blank=True)
    wind_speed = models.FloatField(null=True, blank=True)
    weather_condition = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        response = (f'<{self.__class__.__name__}(city: {self.city}, '
                    f'current_temp: {self.current_temp}, '
                    f'temp_min: {self.temp_min}, temp_max: {self.temp_max}, '
                    f'wind_speed: {self.wind_speed}, '
                    f'weather_condition: {self.weather_condition})>')
        return response
