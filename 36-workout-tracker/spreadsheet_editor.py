import requests
import os


class SpreadsheetEditor():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_info = os.environ['SPREADSHEET_INFO']
        self.sheety_token = os.environ['SHEETY_TOKEN']

    def insert(self):
        headers = {
            'Authorization': 'Bearer ' + self.sheety_token
        }
        payload = {
            'workout': {
                'date': 'xavier',
                'time': '22',
                'exercise': 'test',
                'duration': 'test',
                'calories': 'test'

            }
        }
        response = requests.post(url=self.base_url + self.spreadsheet_info, headers=headers, json=payload)

        print(response.text)
