import requests
import os


class NutritionixAPI():
    def __init__(self):
        self.url = 'https://trackapi.nutritionix.com/v2/natural/exercise'

    def get_exercise_data(self, user_input):
        """
       Args:
           user_input: Details about the exercise

       Returns:
           Response with information about the exercise
       """

        auth_headers = {
            'Content-Type': 'application/json',
            'x-app-id': os.environ['NUTRITIONIX_ID'],
            'x-app-key': os.environ['NUTRITIONIX_KEY']
        }

        body = {
            'query': user_input
        }

        response = requests.post(url=self.url, headers=auth_headers, json=body)
        return response
