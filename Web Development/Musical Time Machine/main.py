from bs4 import BeautifulSoup
import requests

date = input("Which date would you like to travel to? YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
songs_html = response.text

soup = BeautifulSoup(songs_html, "html.parser")
song_title_tags = soup.find_all("h3", class_="a-no-trucate")
# song_artist = soup.find(name="span", class_="a-no-trucate").getText()

song_titles = [" ".join(song.getText().split()) for song in song_title_tags]


print(song_titles)
# print(song_artist)
