from bs4 import BeautifulSoup
import requests
import re

GREATEST_MOVIES_URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(GREATEST_MOVIES_URL)
website = BeautifulSoup(response.text, "html.parser")

movie_titles = [re.sub('\d+\) ', '', title.text) for title in website.find_all('h3')][::-1]


with open("movies.txt", "w") as file:
    for rank, title in enumerate(movie_titles):
        file.write(f"{rank + 1}. {title}\n")
