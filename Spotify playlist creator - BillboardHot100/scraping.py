import requests
from pprint import pprint
from bs4 import BeautifulSoup


def tracks_list(date="#"):
    URL = f"https://www.billboard.com/charts/hot-100/{date}/"
    response = requests.get(url=URL)

    soup = BeautifulSoup(response.text, "html.parser")

    track_tags = soup.find_all(name="h3", class_="a-no-trucate")
    tracks = [track.get_text().strip() for track in track_tags]

    artist_tags = soup.find_all(name="span", class_="a-no-trucate")
    artists = [artist.get_text().strip() for artist in artist_tags]

    queries_list = [f"track:{tracks[x]} artist:{artists[x]}" for x in range(0, len(artists))]
    return queries_list[:10]

# pprint(tracks_list())
