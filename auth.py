# playlist-enhancer
# possibility: customizable based on certain categories?
# artist, obscurity, maybe even album cover?

import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth


def auth():
    with open('config.json', 'r') as config_file:
        config_data = json.load(config_file)

    client_id = config_data['SPOTIPY_CLIENT_ID']
    client_secret = config_data['SPOTIPY_CLIENT_SECRET']
    redirect_uri = config_data['SPOTIPY_REDIRECT_URI']

    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id, client_secret, redirect_uri))
