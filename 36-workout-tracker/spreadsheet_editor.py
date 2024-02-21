import requests
import os


class SpreadsheetEditor():
    def __init__(self):
        self.base_url = 'https://api.sheety.co/'
        self.spreadsheet_info = os.environ['SPREADSHEET_INFO']
