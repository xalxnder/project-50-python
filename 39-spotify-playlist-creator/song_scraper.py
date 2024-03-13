from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


class SongScraper:
    def __init__(self):
        self.BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
        self.response = requests.get(self.BILLBOARD_URL)
        self.website = BeautifulSoup(self.response.text, "html.parser")

    def get_song_info(self):
        """
        Args:
            self: An instance of the SongScraper class.
        Returns:
            list: A list of dictionaries containing the Artists and Songs.


        """
        artist_names = [artist.text.strip() for artist in self.website.find_all(name="span",

                                                                                class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")]
        song_titles = [song.text.strip() for song in self.website.find_all(name="h3",
                                                                           class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only")]

        song_info = pd.DataFrame({
                                           'Artist': artist_names,
                                           'Song': song_titles})
        song_info = song_info.to_dict(orient='records')
        return song_info


