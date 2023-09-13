import math
from datetime import datetime, timedelta

def get_6_months_date():
    current_date = datetime.utcnow()
    six_months_ago = current_date - timedelta(days=6 * 30)
    return six_months_ago.strftime('%Y-%m-%dT%H:%M:%SZ')

def cosine_similarity(list_a, list_b):
    dot_product = sum(a * b for a, b in zip(list_a, list_b))
    magnitude_a = math.sqrt(sum(a ** 2 for a in list_a))
    magnitude_b = math.sqrt(sum(b ** 2 for b in list_b))
    
    if magnitude_a == 0 or magnitude_b == 0:
        return 0.0  # Handle zero division
    
    similarity = dot_product / (magnitude_a * magnitude_b)
    return similarity

def get_average(tracks: list, sp):
    """
    Given a list of tracks, returns a list of length 4,
    describing the average danceability, energy, valence,
    and tempo
    """
    features = [0,0,0,0]

    for track in tracks:
        track_id = track['track']['id']
        audio_features = sp.audio_features([track_id])[0]

        features[0] += audio_features['danceability']/len(tracks)
        features[1] += audio_features['energy']/len(tracks)
        features[2] += audio_features['valence']/len(tracks)
        features[3] += audio_features['tempo']/len(tracks)

    return features