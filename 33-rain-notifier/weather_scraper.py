import requests
import os
import requests
import certifi
import ssl
import geopy.geocoders
import smtplib
from time import strftime, localtime
from geopy.geocoders import Nominatim

# Fixes expired cert issue - https://geopy.readthedocs.io/en/stable/#geopy.geocoders.options.default_ssl_context
ctx = ssl.create_default_context(cafile=certifi.where())
geopy.geocoders.options.default_ssl_context = ctx


# Fixes expired cert issue


class WeatherScraper:
    def __init__(self):
        self.geolocator = Nominatim(user_agent="ISS_Notifier")
        self.WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
        self.CURRENT_LOCATION = self.geolocator.geocode(os.environ['CURRENT_LOCATION'])
        self.CURRENT_LATITUDE = self.CURRENT_LOCATION.latitude
        self.CURRENT_LONGITUDE = self.CURRENT_LOCATION.longitude
        self.rain_count = 0

    def get_current_weather(self):
        """
        Gets the users current weather with the openweathermap api
        Parameters:
            lon - Users longitutde
            lat - Users latitude
            cnt - The amount of timestamps returned by the api
            appid - Openwaethermap api key
        """
        parameters = {'lon': self.CURRENT_LONGITUDE,
                      'lat': self.CURRENT_LATITUDE,
                      'cnt': 4,
                      'appid': self.WEATHER_API_KEY}
        # Add try except here
        try:
            response = requests.get(url='https://api.openweathermap.org/data/2.5/forecast', params=parameters)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('Http Error', e)
        else:
            # print(response['list'])
            return response.json()['list']

    def rain_forecasted(self):
        """
        Checks for rain in the next 12 hours. If 'Drizzle', 'Thunderstorm', or 'Rain' is
        in the response, increment rain count by 1.
        """
        # if not any (self.get_current_weather())
        try:
            for i in self.get_current_weather():
                if i['weather'][0]['main'] in ['Drizzle', 'Thunderstorm', 'Rain']:
                    self.rain_count += 1
        except TypeError as e:
            print(f'Encountered {e}. Ensure your original request returned data.')

    def will_rain(self):
        """
        Checks if rain count is greater than 0. If true, this means rain will occur in the next
        12 hours.
        """
        if self.rain_count > 0:
            print('Hey, its gonna rain at some point')
            return True
        else:
            print('Youre good')
            return False
