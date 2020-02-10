# Weather

##### Requires:
 - Python 3.6+
 - MySQL 5.7+

### Installation

Clone project
```sh
$ git clone https://github.com/TurVova/weather.git
```
Install requirements
```sh
$ pip install -r requirements.txt
```
Add NAME, USER and PASSWORD in the database settings in the settings.py file.

Apply migrations
```sh
$ python manage.py migrate
```
Run server
```sh
$ python manage.py runserver
```
Endpoint `/api/syncWeather` that syncs weather info to a MySQL DB.
Endpoint `/api/currentWeather` that returns the following weather information from DB in a JSON format.

If you want choice another city, use query string parameter `city`. Default city is Dnipro.
