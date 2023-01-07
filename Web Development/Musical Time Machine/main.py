from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv

load_dotenv()

SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

date = input("Which date would you like to travel to? YYYY-MM-DD: ")

billboard_url = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(billboard_url)
songs_html = response.text

soup = BeautifulSoup(songs_html, "html.parser")
song_title_tags = soup.find_all("h3", class_="a-no-trucate")
# song_artist = soup.find(name="span", class_="a-no-trucate").getText()

song_titles = [" ".join(song.getText().split()) for song in song_title_tags]

song_uris = []
year = date.split("-")[0]
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
