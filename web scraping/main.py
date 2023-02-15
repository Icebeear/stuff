import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)
data = response.text
soup = BeautifulSoup(data, "html.parser")
titles = soup.find_all(name="h3", class_="title")

movies = [film.text for film in titles][::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")