import os
import requests
import json


class NewsScraper():
    def __init__(self):
        self.api_key = os.environ['NEWS_API_KEY']
        self.url = 'https://newsapi.org/v2/everything?'
        self.news_brief = ''

    def get_news(self, search_term):
        """
        Retrieves articles from newsapi by searching for the search_term.
        Returns formatted json results
        """
        parameters = {
            'q': search_term,
            'pageSize': 3,
            'sortBy': 'relevancy',
        }

        head = {
            'Authorization': self.api_key,
        }

        response = requests.get(url=self.url, headers=head, params=parameters)
        return response.json()

    def message_generator(self, stock_message, news_response):
        """
        Returns the news brief that will be sent to user
        """
        for item in news_response['articles']:
            self.news_brief += (
                                f"Headline: {item['title']}\n"
                                f"Brief: {item['description']}\n"
                                f"Link To Story: {item['url']}\n"
                                "\n"
                                )
        self.news_brief = f"Subject: {stock_message}\n" + self.news_brief

        return self.news_brief
