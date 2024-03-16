from song_scraper import *
from spotify_interface import *
import webbrowser

spotify_interface = SpotifyInterface()
song_scraper = SongScraper()

user_input = input('Have you already authorized this app? (yes/no)')
if user_input == 'no':
    spotify_interface.request_authorization()
else:
    access_token_check = input('Do you have an access token? (yes/no)')
    if access_token_check == 'no':
        spotify_interface.request_access_token()
    else:
        song_info = song_scraper.get_song_info()
        track_uris = [spotify_interface.get_song_uri(song['Artist'], song['Song']) for i, song in enumerate(song_info) if i < 10]
        spotify_interface.update_playlist(track_uris)

