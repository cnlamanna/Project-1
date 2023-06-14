import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from datetime import date

# Spotify API client
from api_keys import client_id
from api_keys import client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get the current month
current_month = date.today().strftime("%Y-%m")

# Set the start and end dates of the month
start_date = f"{current_month}-01"
end_date = f"{current_month}-31"

# Retrieve the top tracks of the month
top_tracks = sp.playlist_tracks(playlist_id='37i9dQZF1DXcBWIGoYBM5M', market='US', limit=50)['items']

# Loop-de-Lopp, Get the genres for each artist
genres = []
for track in top_tracks:
    for artist in track['track']['artists']:
        artist_info = sp.artist(artist['id'])
        artist_genres = artist_info.get('genres', [])
        if artist_genres:
            genres += artist_genres

# Filter out genres where the genre list is empty
filtered_genres = [genre for genre in genres if genre]

# Count the number of times each genre occurs
genre_counts = {}
for genre in filtered_genres:
    genre_counts[genre] = genre_counts.get(genre, 0) + 1

# Sort genres by count in descending order
sorted_genres = sorted(genre_counts, key=genre_counts.get, reverse=True)

# Retrieve the top three genres
top_genres = sorted_genres[:3]

# Print the top genres
print(f"Top Genres of {current_month}:")
for genre in top_genres:
    print(genre)