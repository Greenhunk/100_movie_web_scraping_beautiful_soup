import requests
from bs4 import BeautifulSoup
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")

movie_web_page = response.text
soup = BeautifulSoup(movie_web_page, "html.parser")
movie_name_list = soup.find_all(name="h3", class_="title")
movie_name_list_1 =[]

for movie in movie_name_list:
    movie_name = movie.getText()
    movie_name_list_1.append(movie_name)

movie_name_reverse = movie_name_list_1[::-1]

with open("movie_name_list.txt", "w", encoding="utf-8") as file:
    for name in movie_name_reverse:
        file.write(str(f"{name} \n"))
