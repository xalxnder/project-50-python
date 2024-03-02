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
