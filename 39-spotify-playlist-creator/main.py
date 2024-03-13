from song_scraper import *
from spotify_interface import *
import webbrowser

spotify_interface = SpotifyInterface()
# spotify_interface.request_authorization()
# spotify_interface.request_access_token()
spotify_interface.get_tracks()
spotify_interface.get_refresh_token()


