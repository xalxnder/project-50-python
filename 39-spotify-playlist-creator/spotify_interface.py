import requests
import os
import random
import string
import base64
import webbrowser


class SpotifyInterface:
    def __init__(self):
        self.CLIENT_ID = os.environ.get('SPOTIFY_CLIENT_ID')
        self.CLIENT_SECRET = os.environ.get('SPOTIFY_CLIENT_SECRET')
        self.AUTH_URL = 'https://accounts.spotify.com/authorize'
        self.CODE = os.environ.get('CODE')
        self.STATE = os.environ.get('STATE')
        self.refresh_token = os.environ.get('SPOTIFY_REFRESH_TOKEN')
        self.access_token = self.get_refresh_token()

    # Generate a random string for the state parameter
    def generate_state(self):
        length = 10
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def get_auth_base64(self):
        """Used to encode our Client ID and Client Secret when retriving your refresh token"""
        message = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        auth_header = {
            "Authorization": "Basic" + " " + base64_message}
        return auth_header

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

    def request_access_token(self):
        message = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        print(base64_message)

        body = {
            'grant_type': 'authorization_code',
            # YOU CAN ONLY USE CODE ONCE.#
            'code': self.CODE,
            'redirect_uri': 'https://example.com',
        }
        headers = {
            "Authorization": "Basic" + " " + base64_message,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post('https://accounts.spotify.com/api/token', data=body, headers=headers)
        print(response.json())
        return response.json()

    def get_tracks(self):
        auth_header = {
            'Authorization': 'Bearer ' + self.access_token}
        response = requests.get('https://api.spotify.com/v1/tracks/2TpxZ7JUBn3uw46aR7qd6V', headers=auth_header)
        print(response.json())

    def get_refresh_token(self):
        message = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        body = {
            'grant_type': 'refresh_token',
            'refresh_token': self.refresh_token
        }

        headers = {
            "Authorization": "Basic" + " " + base64_message,
            'Content-Type': 'application/x-www-form-urlencoded'
        }

        response = requests.post('https://accounts.spotify.com/api/token', data=body, headers=headers)
        return response.json()['access_token']


