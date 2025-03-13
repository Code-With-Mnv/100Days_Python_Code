import requests
from bs4 import BeautifulSoup

response = requests.get(
    url="https://www.empireonline.com/movies/features/best-movies-2/"
)

data = response.text

soup_data = BeautifulSoup(data, "html.parser")

movie_tags_list = soup_data.find_all(
    name="h3", class_="listicleItem_listicle-item__title__BfenH"
)

rev_movies_list = [movie_tag.getText() for movie_tag in movie_tags_list]
movie_list = rev_movies_list[::-1]


with open("movies.txt", "w") as wrtxt:
    for movie in movie_list:
        wrtxt.write(movie + "\n")
