import spotipy
import json
import datetime
from spotipy.oauth2 import SpotifyOAuth
from collections import defaultdict

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)

sp_oauth = SpotifyOAuth(
    client_id = config_data['SPOTIPY_CLIENT_ID'],
    client_secret = config_data['SPOTIPY_CLIENT_SECRET'],
    redirect_uri = config_data['SPOTIPY_REDIRECT_URI'],
    scope='user-top-read'
)
sp = spotipy.Spotify(auth_manager=sp_oauth)

def generate_top_tracks(time_range):
    """
    Simple generator for top tracks
    """
    response = sp.current_user_top_tracks(limit = 50, time_range=time_range)
    for track in response['items']:
        yield track

def generate_combined_top_tracks():
    short_generator = generate_top_tracks('short_term')
    medium_generator = generate_top_tracks('medium_term')
    
    combined_tracks = set()
    for i in range(50):
        try:
            track = next(short_generator)
            track_id = track['id']
            if track_id not in combined_tracks:
                yield track
                combined_tracks.add(track_id)
        except StopIteration:
            print("short tracks exhausted")

        try:
            track = next(medium_generator)
            track_id = track['id']
            if track_id not in combined_tracks:
                yield track
                combined_tracks.add(track_id)
        except StopIteration:
            print("medium tracks exhausted")
    
    

def create_playlist(danceability=None, energy=None, valence=None, acous=None, inst=0):
    pass


if __name__ == "__main__":
    pass