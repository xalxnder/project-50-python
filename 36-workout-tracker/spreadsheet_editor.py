import requests
import os
from datetime import date, datetime


class SpreadsheetEditor():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_info = os.environ['SPREADSHEET_INFO']
        self.sheety_token = os.environ['SHEETY_TOKEN']
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

    def insert(self, data):
        """
        Args:
            data: Exercise data returned from the nutritionix_api

        Returns:
            Returns response from sheety API
        """
        print(len(data))
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }
        for i in data['exercises']:
            self.exercise = i['name']
            self.duration = i['duration_min']
            self.calories = i['nf_calories']

            payload = {
                'workout': {
                    'date': self.today.strftime('%m/%d/%Y'),
                    'time': self.time_converter(self.duration),
                    'exercise': self.exercise,
                    'duration': self.time_converter(self.duration),
                    'calories': self.calories

                }
            }

            response = requests.post(url=self.base_url + self.spreadsheet_info, headers=headers, json=payload)

        return response
