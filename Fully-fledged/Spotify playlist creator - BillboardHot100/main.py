import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from scraping import tracks_list
from dotenv import load_dotenv
import os

load_dotenv()
#################################################################
#################################################################

#   DUE TO API ENDPOINT QUERY LIMITS ONLY THE FIRST 10 SONGS
#   FROM BILLBOARD HOT 100 WILL BE ADDED TO YOUR NEW PLAYLIST

#################################################################
#################################################################


    # AUTHENTICATION SECTION
authenticator = SpotifyOAuth(client_id=os.environ.get('CLIENT_ID'),
                             client_secret=os.environ.get('CLIENT_SECRET'),
                             redirect_uri="http://example.com",
                             scope="playlist-read-private,"
                                   "playlist-modify-private,"
                                   "user-read-private",
                             username=os.environ.get('USERNAME'))
                             # cache_path=os.environ.get('CACHE_PATH'))

# authenticator.get_access_token(as_dict=False)
sp = spotipy.Spotify(auth_manager=authenticator)


    # GET THE USER ID
user_id = sp.current_user()["id"]

#########################################################################################################

    # ASK THE USER FOR A DATE FOR WHICH THE BILLBOARD RANKING SHOULD BE FOUND
    # SCRAP BILLBOARD HOT 100 WEBSITE FOR TRACKS & THEIR AUTHORS

while True:
    date = input("Which date do you want the 'Billboard Hot 100' ranking for? (in format RRRR-MM-DD)\n"
                 "If you want the current ranking just hit enter. ")

    if date != "":
        if int(date.split("-")[0]) < 2010:
            print("Sorry, the data is available only from 2010.\n")
        else:
            queries_list = tracks_list(date=date)
            break
    else:
        queries_list = tracks_list()
        break

#########################################################################################################


    # FUNCTIONS FOR THE "PLAYLIST CREATE MECHANISM"
n = 0
def similar_playlist_exists():
    global n
    # GET USER'S CURRENT PLAYLISTS
    current_playlists = sp.user_playlists(
        user=user_id,
        limit=10,
    )

    if current_playlists["items"] != []:
        for playlist in current_playlists["items"]:
            if "100 hits" in playlist["name"]:
                n += 1

    if n != 0:
        return True
    else:
        return False


def create_playlist(playlist_name):
    sp.user_playlist_create(
        user=user_id,
        name=playlist_name,
        public=False,
        collaborative=False,
        description="Playlist includes 100 hits listed"
                    "in a given 'Billboard Hot 100' ranking"
    )

#########################################################################################################

    # PLAYLIST CREATE MECHANISM
if similar_playlist_exists():
    should_continue = input("Playlist with similar name ('100 hits') already exists. "
                            "Do you wish to continue and create a new one? [Yes/No]: ")
    if should_continue.lower() == "yes":
        change_name = input("Would you like to change the playlist's name? [Yes/No]: ")
        if change_name.lower() == "yes":
            new_name = input("Enter the new name: ")
            create_playlist(playlist_name=new_name)
        else:
            new_name = f"100 hits #{n+1}"
            create_playlist(playlist_name=new_name)
    else:
        print("Shutting down...")
        exit()
else:
    new_name = "100 hits"
    create_playlist(playlist_name=new_name)

#########################################################################################################


    # FUNCTIONS FOR THE "ADD TRACKS TO PLAYLIST MECHANISM"
def playlist_id():
    current_playlists_new = sp.user_playlists(user=user_id, limit=10)

    for playlist in current_playlists_new["items"]:
        if new_name == playlist["name"]:
            return playlist["id"]


def track_id(query):
    query = sp.search(
        q=query,
        type="track",
        limit=1
    )
    try:
        return query["tracks"]["items"][0]["uri"]
    except IndexError:
        return "Track not found"


##########################################################################################
print("Working...")

    # ADD TRACKS TO PLAYLIST MECHANISM
hits_id_list = []

for query in queries_list:
    hit_id = track_id(query=query)
    if hit_id != "Track not found":
        hits_id_list.append(hit_id)

sp.playlist_add_items(
    playlist_id=playlist_id(),
    items=hits_id_list,
)

if len(hits_id_list) < 10:
    print(f"Finished. Unfortunately some tracks ({10-len(hits_id_list)}) were not found.")
else:
    print("Finished. All tracks have been successfully added to your new playlist.")
##########################################################################################










