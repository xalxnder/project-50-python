import requests
import os
from datetime import date, datetime


class SpreadsheetInterface():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_id = os.environ['FLIGHT_SPREADSHEET']
        self.sheety_token = os.environ['FLIGHT_SHEETY_TOKEN']
        self.today = date.today()

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

    def read(self, sheet_name):
        """
        Returns:
            Returns response from sheety API
        """
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }

        try:
            response = requests.get(url=self.base_url + self.spreadsheet_id + sheet_name, headers=headers)
            response.raise_for_status()
            # print(response.json())
        except requests.exceptions.HTTPError as e:
            print('Http Error', e)
        data = response.json()[sheet_name]
        return data

    def update_iata_codes(self, row, code, sheet_name):
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

        response = requests.put(url=self.base_url + self.spreadsheet_id + sheet_name + '/' + str(row), headers=headers,
                                json=payload)
        print(response.json())
        return response

    def add_users(self, first_name, last_name, email, sheet_name):

        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }

        payload = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': email

            }
        }

        response = requests.post(url=self.base_url + self.spreadsheet_id + sheet_name, headers=headers, json=payload)
        print(response.json())
        return response
