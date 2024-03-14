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
        self.playlist_id = os.environ.get('SPOTIFY_PLAYLIST_ID')
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
        """
        Request authorization from the user to access their Spotify account.
        Returns:
            str: The URL to the redirect uri which contains the code needed to obtain an access token.
        """
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
        """
        Request an access token from Spotify using the code obtained from the request_authorization method.
        Returns:
            dict: A dictionary containing the access token and refresh token.

        """
        message = f"{self.CLIENT_ID}:{self.CLIENT_SECRET}"
        message_bytes = message.encode("ascii")
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode("ascii")
        print(base64_message)

        body = {
            'grant_type': 'authorization_code',
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

    def get_refresh_token(self):
        """
        Get a new access token using the refresh token.
        Returns:
            str: The new access token.

        """
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

    def get_song_uri(self, artist, song):
        headers = {
            'Authorization': 'Bearer ' + self.access_token}
        parameters = {
            'q': artist + ' ' + song,
            'type': 'track',
            'limit': 1
        }
        response = requests.get('https://api.spotify.com/v1/search', headers=headers, params=parameters)
        track_uri = response.json()['tracks']['items'][0]['uri']
        print(response)
        return track_uri

    def update_playlist(self, track_uris):
        headers = {
            'Authorization': 'Bearer ' + self.access_token,
            'Content-Type': 'application/json'
        }

        data = {
            'uris': track_uris,
        }

        response = requests.put(f'https://api.spotify.com/v1/playlists/{self.playlist_id}/tracks', headers=headers, json=data)
        print(response.json())

