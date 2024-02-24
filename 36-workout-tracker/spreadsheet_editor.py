import requests
import os
from datetime import date


class SpreadsheetEditor():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_info = os.environ['SPREADSHEET_INFO']
        self.sheety_token = os.environ['SHEETY_TOKEN']
        self.today = date.today()
        self.exercise = ''
        self.duration = ''

    @staticmethod
    def time_converter(time):
        hours = int(time) // 60
        minutes = int(time) % 60
        if time > 60:
            return f'{hours}:{minutes}:00'
        else:
            return f'{minutes}:00.00'

    def insert(self, data):
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }
        for i in data['exercises']:
            self.exercise = i['name']
            self.duration = i['duration_min']

        payload = {
            'workout': {
                'date': self.today,
                'time': self.time_converter(self.duration),
                'exercise': self.exercise,
                'duration': 'test',
                'calories': 'test'

            }
        }
        response = requests.post(url=self.base_url + self.spreadsheet_info, headers=headers, json=payload)

        print(response.text)
