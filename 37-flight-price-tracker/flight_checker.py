import requests
import os


class FlightChecker:
    def __init__(self):
        self.api_key = os.environ['KIWI_API_KEY']
        self.url = os.environ['KIWI_ENDPOINT']
        self.prices = {}

    def get_code(self, city):
        """

        Args:
            city: Name of city departure city where airport is located

        Returns:
            string: IATA code for the city

        """
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

    def get_prices(self, origin, destination, start_date, end_date):
        """

        Args:
            origin: IATA code of the origin airport
            destination: IATA code of the destination airport
            start_date: Date when user plans on departing
            end_date: Date when user plans on returning

        Returns:
            dictionary: Destination IATA codes and the cheapest flights

        """
        head = {
            'apikey': self.api_key,
        }
        parameters = {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': start_date,
            'date_to': end_date,
            'curr': 'USD',
            'one_for_city': 1,
            "nights_in_dst_from": 1,
            "nights_in_dst_to": 28,
            'max_stopovers': 0,
        }

        response = requests.get(url=self.url + 'search', headers=head, params=parameters)
        try:
            data = response.json()['data'][0]
        except IndexError as e:
            print(e)
            print(f'Unable to get price for {destination}')
        else:
            self.prices.update({
                                             destination: data['price']})
            return self.prices
