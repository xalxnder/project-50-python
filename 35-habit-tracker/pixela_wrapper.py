import requests
import os
from datetime import date


class PixelaAPI():
    def __init__(self):
        self.user_url = 'https://pixe.la/v1/users'
        self.username = os.environ['PIXELA_USERNAME']
        self.token = os.environ['PIXELA_TOKEN']
        self.date = self.get_date()

    def create_user(self):
        request_body = {
            'token': self.token,
            'username': self.username,
            'agreeTermsOfService': 'yes',
            'notMinor': 'yes'
        }

        response = requests.post(url=self.user_url, json=request_body)
        print(response)
        print(response.text)

    def create_graph(self):
        request_header = {
            'X-USER-TOKEN': self.token
        }

        request_body = {
            'id': 'coding',
            'name': 'Coding',
            'unit': 'hour',
            'type': 'int',
            'color': 'sora',
            'timezone': 'America/New_York'
        }
        response = requests.post(url=self.user_url + '/' + self.username + '/graphs', headers=request_header,
                                 json=request_body)
        print(response.text)

    def add_point(self):
        request_header = {
            'X-USER-TOKEN': self.token
        }
        request_body = {
            'date': self.date,
            'quantity': '3'
        }
        response = requests.post(url='https://pixe.la/v1/users/hixavier/graphs/coding', headers=request_header,
                                 json=request_body)
        print(response.text)

    @staticmethod
    def get_date():
        today = str(date.today())
        return today.replace('-', '')
        pass
