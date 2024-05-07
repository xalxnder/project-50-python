import requests
import os

class MovieAPI:
    def __init__(self):
        self.API_KEY = os.environ['MOVIE_API_TOKEN']

    def search(self, movie):
        url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"

        headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {self.API_KEY}"
        }
        parameters = {
            'query': movie
        }

        response = requests.get(url, headers=headers, params=parameters).json()
        results = response['results']
        cleaned_up_results = [{
                                  'title': x['original_title'],
                                  'image_url': f'https://image.tmdb.org/t/p/w500/{x["poster_path"]}',
                                'year': x['release_date'].split('-')[0],
                                'description': x['overview']
        } for x in results]
        return cleaned_up_results


