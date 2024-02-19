import os
import requests
from datetime import date
from datetime import timedelta


class StockScraper:
    def __init__(self):
        self.url = 'https://www.alphavantage.co/query'
        self.symbol = 'IBM'
        self.function = 'TIME_SERIES_DAILY'
        self.interval = '60min'
        self.apikey = os.environ['STOCKS_API_KEY']
        self.closed_days = ['Saturday', 'Sunday']
        self.off_days = {
            'Sunday':[2,3],
            'Monday': [3,3],
            'Tuesday': [1,4]
        }
        self.today = date.today().strftime("%A")

    def get_stock_data(self):
        """
        Gets response from the alphavantage api, which consists of daily stock data
        """
        parameters = {
            'symbol': self.symbol,
            'function': self.function,
            'interval': self.interval,
            'apikey': self.apikey
        }
        # print(parameters['apikey'])
        try:
            response = requests.get(url=self.url, params=parameters)
            response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print('Http Error', e)
        try:
            return response.json()['Time Series (Daily)']
        except KeyError as e:
            print(e)

    def get_opening_closing(self, stock_data):
        """
        Takes the response from the alphavantage api, and gets the closing values from yesterday, and two days ago.
        First checks if today is, Sunday, Monday, or Tuesday since yeserday, and two days ago in relation to those days
        falls on a weekend.
        """
        if self.today in self.off_days:
            yesterday = date.today() - timedelta(days=self.off_days[self.today][0])
            two_days_ago = date.today() - timedelta(days=self.off_days[self.today][1])
        else:
            yesterday = date.today() - timedelta(days=1)
            two_days_ago = date.today() - timedelta(days=2)
        yesterdays_stock_data = stock_data[str(yesterday)]['4. close']
        two_days_ago_stock_data = stock_data[str(two_days_ago)]['4. close']
        print(
            f"Yesterday - {yesterday}:{yesterdays_stock_data} \n2 Days Ago - {two_days_ago}:{two_days_ago_stock_data}")
        return two_days_ago_stock_data, yesterdays_stock_data

    def market_closed(self):
        """
        Checks if market is open or not.
        """
        if self.today in self.closed_days:
            return True
        else:
            return False

    # @staticmethod
    def get_difference(self, closing):
        """Calculates difference between yesterday and today's closing values"""
        two_days_ago_price = float(closing[0])
        print(two_days_ago_price)
        yesterdays_price = float(closing[1])
        print(yesterdays_price)
        difference = yesterdays_price - two_days_ago_price
        arrow = ''

        if yesterdays_price > two_days_ago_price:
            arrow = ''
            print(f'There was an {difference} increase. Yay!')
            arrow = '🔺'
        else:
            print(f'There was a {difference} decrease :( ')
            arrow = '🔻'
        percentage_difference = abs(difference / two_days_ago_price) * 100
        message = f" {self.symbol} {arrow} {percentage_difference:.2f}%"
        return message

        # print(float(closing[0]) - float(closing[1]))

    @staticmethod
    def market_hours():
        print(('Monday: 9:30 AM – 4 PM ET \n'
               'Tuesday: 9:30 AM – 4 PM ET \n'
               'Wednesday: 9:30 AM – 4 PM ET \n'
               'Thursday: 9:30 AM – 4 PM ET \n'
               'Friday: 9:30 AM – 4 PM ET \n'
               'Saturday: CLOSED \n'
               'Sunday: CLOSED \n'
               ))
