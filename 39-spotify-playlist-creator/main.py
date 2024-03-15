from song_scraper import *
from spotify_interface import *
import webbrowser

spotify_interface = SpotifyInterface()
song_scraper = SongScraper()



if spotify_interface.is_authorized():
    pass
else:
    spotify_interface.request_authorization()
    spotify_interface.request_access_token()


# spotify_interface.request_authorization()
# spotify_interface.request_access_token()

# song_info = song_scraper.get_song_info()
# print(song_info[0]['Artist'])
# print(song_info[0]['Song'])

# spotify_interface.get_song_uri(song_info[0]['Artist'], song_info[0]['Song'])
# track_uris = [spotify_interface.get_song_uri(song['Artist'], song['Song']) for song in song_info]
# track_uris = [spotify_interface.get_song_uri(song['Artist'], song['Song']) for i, song in enumerate(song_info) if i < 10]
#
# print(track_uris)


# spotify_interface.update_playlist(track_uris)
