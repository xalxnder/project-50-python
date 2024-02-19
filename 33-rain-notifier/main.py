from weather_scraper import *
from message_sender import *

scraper = WeatherScraper()
scraper.rain_forecasted()


if scraper.will_rain():
    sender = MessageSender('Hey')
    sender.send_message()
