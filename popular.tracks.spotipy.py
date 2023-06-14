import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Set up the Spotify API client
from api_keys import client_id
from api_keys import client_secret

# Authenticate with the Spotify API
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

# Define the genre you want to retrieve data for
genre = 'rock'  # Replace with your desired genre

# Get the category ID for the genre
categories = sp.categories(country='US', limit=50)
category_id = None
for category in categories['categories']['items']:
    if category['name'].lower() == genre.lower():
        category_id = category['id']
        break

# Retrieve the playlists in the genre category
playlists = sp.category_playlists(category_id, country='US', limit=50)

# Get the first playlist ID in the genre category
playlist_id = playlists['playlists']['items'][0]['id']

# Get the playlist tracks
tracks = sp.playlist_tracks(playlist_id)

# Extract the artist information from the tracks
artists = []
for track in tracks['items']:
    artist_names = [artist['name'] for artist in track['track']['artists']]
    artists.extend(artist_names)

# Count the number of artists in each genre
artist_count = {}
for artist in artists:
    if artist in artist_count:
        artist_count[artist] += 1
    else:
        artist_count[artist] = 1

# Print the number of artists in each genre
for artist, count in artist_count.items():
    print(f'{artist}: {count}')
