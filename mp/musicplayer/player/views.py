from django.shortcuts import render
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def index(request):
    # Replace these with your Spotify API credentials
    client_id = "YOUR_SPOTIFY_CLIENT_ID"
    client_secret = "YOUR_SPOTIFY_CLIENT_SECRET"

    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
        client_id=client_id,
        client_secret=client_secret
    ))

    # Example playlist: Today’s Top Hits
    results = sp.playlist_items("37i9dQZF1DXcBWIGoYBM5M", additional_types=['track'], limit=5)

    songs = []
    for item in results['items']:
        track = item['track']
        songs.append({
            'name': track['name'],
            'artist': track['artists'][0]['name'],
            'preview_url': track['preview_url'] or '',  # 30-sec preview
            'album_art': track['album']['images'][0]['url']
        })

    return render(request, "player/index.html", {"songs": songs})
