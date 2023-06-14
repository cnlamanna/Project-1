import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Set up the Spotify API client
from api_keys import client_id
from api_keys import client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Define the genres for which you want to retrieve the top artists
genres = ['rock', 'pop', 'country']

# Loop through each genre and retrieve the top artists
for genre in genres:
    # Search for the genre and get the first result
    results = sp.search(q='genre:' + genre, type='artist', limit=5)
    artists = results['artists']['items']
    
    # Extract the top artists' names
    top_artists = [artist['name'] for artist in artists]
    
    # Print the genre and the top artists
    print(f"Top Artists in {genre}:")
    for artist in top_artists:
        print(artist)
    print()