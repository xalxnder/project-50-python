import requests
import os


class MovieAPI():
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
            'title': movie['original_title'],
            'image_url': f'https://image.tmdb.org/t/p/w500/{movie["poster_path"]}',
            'year': movie['release_date'].split('-')[0],
            'description': movie['overview'],
            'id': movie['id']
        } for movie in results]
        print(cleaned_up_results)
        return cleaned_up_results
