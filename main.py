import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict
from calculations import *

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

sp_oauth = SpotifyOAuth(
    client_id = config_data['SPOTIPY_CLIENT_ID'],
    client_secret = config_data['SPOTIPY_CLIENT_SECRET'],
    redirect_uri = config_data['SPOTIPY_REDIRECT_URI'],
    scope='playlist-read-private',
)
GLOBAL_SP = spotipy.Spotify(auth_manager=sp_oauth)


if __name__ == "__main__":
    # playlists = GLOBAL_SP.current_user_playlists()
    # for playlist in playlists['items']:
    #     print(playlist['name'])
    playlist_url = "https://open.spotify.com/playlist/6ITIADGiyM8gJtB7XF3dIO?si=7baef8e65eee4047"
    test_tracks = GLOBAL_SP.playlist_tracks(playlist_url)['items']
    for feature in get_average(test_tracks, GLOBAL_SP):
        print(feature)
