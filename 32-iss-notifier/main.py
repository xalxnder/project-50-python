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

geolocator = Nominatim(user_agent="ISS_Notifier")
CURRENT_LOCATION = geolocator.geocode("") # Your address
CURRENT_LATITUDE = CURRENT_LOCATION.latitude
CURRENT_LONGITUDE = CURRENT_LOCATION.longitude
ISS_DATA = requests.get(url='http://api.open-notify.org/iss-now.json').json()
ISS_LONGITUDE = float(ISS_DATA['iss_position']['longitude'])
ISS_LATITUDE = float(ISS_DATA['iss_position']['latitude'])
EMAIL_PASSWORD=''
SENDER_EMAIL = ''
RECIPIENT_EMAIL = ''


def iss_in_proximity():
    """Check if our current longitude and latitude are with 5 of the ISS longitude and latitude"""
    if ISS_LONGITUDE - 5 < CURRENT_LONGITUDE < ISS_LONGITUDE + 5 and ISS_LATITUDE - 5 < CURRENT_LATITUDE < ISS_LATITUDE + 5:
        print("IN RANGE")
        return True


epoch = ISS_DATA['timestamp']
formatted_time = strftime('%H:%M:%S %p', localtime(epoch)).replace('0', '', 1)
iss_timestamp = formatted_time.split(':')[0]

SUNRISE_SUNSET_PARAMS = {
    'lat': CURRENT_LATITUDE,
    'lng': CURRENT_LONGITUDE,
    'tzid': 'America/New_York',
    'formatted': 0
}

print(float(CURRENT_LONGITUDE) - float(ISS_LONGITUDE))
# Check if dark outside
sunrise_data = requests.get(url='https://api.sunrise-sunset.org/json', params=SUNRISE_SUNSET_PARAMS).json()
SUNRISE = int(sunrise_data['results']['sunrise'].split('T')[1].split(':')[0])
SUNSET = int(sunrise_data['results']['sunset'].split('T')[1].split(':')[0])


def is_dark_outside():
    """Checks if iss timestamp is not in the range of Sunrise and Sunset times."""
    if iss_timestamp not in range(SUNRISE, SUNSET):
        return True


if is_dark_outside() and iss_in_proximity():
    password = ""
    connection = smtplib.SMTP("smtp.gmail.com", port=587)
    connection.starttls()
    connection.login(user=SENDER_EMAIL, password=EMAIL_PASSWORD)
    connection.sendmail(from_addr=SENDER_EMAIL, to_addrs=RECIPIENT_EMAIL, msg='Look up!!')
    connection.close()
