import requests
import os


class FlightChecker():
    def __init__(self):
        self.api_key = os.environ['KIWI_API_KEY']
        self.url = os.environ['KIWI_ENDPOINT']

    def get_code(self, city):
        head = {
            'apikey': self.api_key,
        }
        parameters = {
            'term': city,
            'location_types': 'city'
        }

        response = requests.get(url=self.url + 'locations/query', headers=head, params=parameters)
        results = response.json()['locations']

        code = results[0]['code']
        return code

    def get_prices(self):
        head = {
            'apikey': self.api_key,
        }
        parameters = {
            'fly_from': 'PHL',
            'fly_to': 'TYO',
            'date_from': '04/04/2024',
            'date_to': '04/10/2024',
            'curr': 'USD',
            'limit': 5,
            # 'price_from': 0,
            # 'price_to':485
            'sort':'price',
            'max_stopovers': 0
        }

        response = requests.get(url=self.url + 'search', headers=head, params=parameters)
        print(response.json())

