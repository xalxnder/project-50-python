from song_scraper import *
from spotify_interface import *
import webbrowser

spotify_interface = SpotifyInterface()
song_scraper = SongScraper()
# spotify_interface.request_authorization()
# spotify_interface.request_access_token()
# spotify_interface.get_tracks()

print(song_scraper.get_artist_name())


