from bs4 import BeautifulSoup
import requests

date = input("Which date would you like to travel to? YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
songs_html = response.text

soup = BeautifulSoup(songs_html, "html.parser")
song_title = soup.select_one(selector="h3 a").getText()
song_artist = soup.find(name="span", class_="a-no-trucate").getText()
print(song_title)
print(song_artist)
