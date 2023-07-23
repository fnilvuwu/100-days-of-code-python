import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)

archive_web = response.text
soup = BeautifulSoup(archive_web, "html.parser")
movie_title_list = soup.find_all(name="h3", class_="title")

with open("movies.txt", "w") as file:
    for title in movie_title_list[::-1]:
        file.write(f"{title.getText()}\n")

    #another way
    # for i in range(len(movie_title_list) - 1, -1, -1):
    #     file.write(f"{movie_title_list[i].getText()}\n")