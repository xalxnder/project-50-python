import requests
import os
from datetime import date, datetime


class SpreadsheetEditor():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_info = os.environ['FLIGHT_SPREADSHEET']
        self.sheety_token = os.environ['FLIGHT_SHEETY_TOKEN']
        self.today = date.today()
        self.exercise = ''
        self.duration = ''
        self.calories = ''

    @staticmethod
    def time_converter(time):
        """

        Args:
            time: Exercise duration in minutes

        Returns:
            Time formatted as mm:ss or hh:mm:ss

        """
        hours = int(time) // 60
        minutes = int(time) % 60
        if time > 60:
            return f'{hours}:{minutes:02}:00'
        else:
            return f'{minutes}:00'

    def read(self):
        """
        Returns:
            Returns response from sheety API
        """
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }

        payload = {
            'price': {
                'city': 'test',
                'iataCode': 'TEST',
                'lowestPrice': 55,
            }
        }
        try:
            response = requests.get(url=self.base_url + self.spreadsheet_info, headers=headers, json=payload)
            response.raise_for_status()
            # print(response.json())
        except requests.exceptions.HTTPError as e:
            print('Http Error', e)
        print(response.json())
        return response.json()

    def update_iata_codes(self, row, code):
        """
        Returns:
            Returns response from sheety API
        """
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }

        payload = {
            'price': {
                'iataCode': code,


            }
        }

        response = requests.put(url=self.base_url + self.spreadsheet_info + '/'+str(row), headers=headers, json=payload)
        print(response.json())
        return response
