import requests
import os
import random
import string
import webbrowser


class SpotifyInterface:
    def __init__(self):
        self.CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
        self.CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.AUTH_URL = 'https://accounts.spotify.com/authorize'
        self.CODE = os.environ.get('CODE')
        self.STATE = os.environ.get('STATE')

    # Generate a random string for the state parameter
    def generate_state(self):
        length = 10
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def request_authorization(self):
        parameters = {
            'client_id': self.CLIENT_ID,
            'response_type': 'code',
            'state': self.generate_state(),
            'redirect_uri': 'https://example.com',
            'scope': 'playlist-modify-private playlist-modify-public playlist-read-private'
        }
        response = requests.get(self.AUTH_URL, params=parameters)
        print(response.url)
        return response.url



    def get_access_token(self):
        pass
