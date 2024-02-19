from stock_scraper import *
from news_scraper import *
from message_sender import *
from datetime import date



news = NewsScraper()
stocks = StockScraper()
message_sender = MessageSender()

if stocks.market_closed():
    print('Market is closed today. Using the closing values from the two closest previous days. \n Please see '
          'official hours, below: \n')
    stocks.market_hours()

stock_data = stocks.get_stock_data()
closing_values = stocks.get_opening_closing(stock_data)

news_response= news.get_news('IBM')
stock_message = stocks.get_difference(closing_values)
news_brief = news.message_generator(stock_message, news_response)
message_sender.send_message(news_brief)

