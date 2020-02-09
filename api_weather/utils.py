import json

import requests
from django.conf import settings


def get_weather(city: str) -> dict:
    """
    Get weather data from open weather map

    :param city: name of the city for which we receive data
    :return: weather data or blank dict
    """
    URL = (
        f'{settings.OPEN_WEATHER_MAP["url"]}?q={city}&'
        f'appid={settings.OPEN_WEATHER_MAP["api_key"]}&units=metric'
    )
    request = requests.get(url=URL)
    response = json.loads(request.text) if request.status_code == 200 else {}

    return response
