import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Spotify API client
from api_keys import client_id
from api_keys import client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# input genres to search for 
genres = ['rock', 'pop', 'rap']

# Loop-de-Loop through each genre and retrieve  top artists
for genre in genres:
    # Search for the genre and get 
    results = sp.search(q='genre:' + genre, type='artist', limit=5)
    artists = results['artists']['items']
    
    # get the top artist names
    top_artists = [artist['name'] for artist in artists]
    
    # Print the genre and the top artists
    print(f"Top Artists in {genre}:")
    for artist in top_artists:
        print(artist)
    print()