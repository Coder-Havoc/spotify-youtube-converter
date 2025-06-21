# spotify/spotify_client.py

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv("SPOTIPY_CLIENT_ID")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET")

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

def get_spotify_tracks(playlist_url):
    tracks = []
    results = sp.playlist_tracks(playlist_url)
    
    while results:
        for item in results["items"]:
            track = item["track"]
            track_name = track["name"]
            artist_name = track["artists"][0]["name"]
            full_name = f"{track_name} - {artist_name}"
            tracks.append(full_name)
        
        if results["next"]:
            results = sp.next(results)
        else:
            break

    return tracks
