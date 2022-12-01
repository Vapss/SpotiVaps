# Checking users followers
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth


if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Whoops, need a username!")
    print("usage: python user_playlists.py [username]")
    sys.exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth())

followers = sp.user_follow_users(username)

for follower in followers['items']:
    print(follower['name'])