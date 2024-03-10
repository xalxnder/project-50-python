from bs4 import BeautifulSoup
import requests
import re



class SongScraper:
    def __init__(self):
        self.BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
        self.response = requests.get(self.BILLBOARD_URL)
        self.website = BeautifulSoup(self.response.text, "html.parser")


    def get_artist_name(self):
        artist_names = [artist.text.strip() for artist in self.website.find_all(name="span",
                                                                                     class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
        return artist_names

    def get_song_title(self):
        song_titles = [song.text.strip() for song in self.website.find_all(name="h3",
                                                                     class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]

        return song_titles

