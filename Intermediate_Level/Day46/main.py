import requests
import spotipy
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyOAuth

date = input(
    "Which year do you want to travel to? Type the date in this format YYYY-MM-DD: "
)

access_2_site = requests.get("https://www.billboard.com/charts/hot-100/" + date)

raw_soup = BeautifulSoup(access_2_site.text, "html.parser")
song_tags = raw_soup.select("li ul li h3")
song_names = [song_tag.getText().strip() for song_tag in song_tags]


sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="YOUR UNIQUE CLIENT ID",
        client_secret="YOUR UNIQUE CLIENT SECRET",
        show_dialog=True,
        cache_path="token.txt",
        username="YOUR SPOTIFY DISPLAY NAME",
    )
)

user_id = sp.current_user()["id"]

song_uris = []
year = date.split("-")[0]
for song in song_names:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

playlist = sp.user_playlist_create(
    user=user_id, name=f"{date.split("-")[0]}'s TOP 100", public=False
)

sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)

print("Your playlist has been generated!")
