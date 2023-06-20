import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#PREMISE OF CODE: pulls top 3 popular genres from spotify. this is a "live" pull, as it produces different genres each time it is run
# Spotify API client
from api_keys import client_id
from api_keys import client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Get available genre seeds
response = sp.recommendation_genre_seeds()
genre_seeds = response['genres']

# Calculate the popularity score for each genre
genre_popularity = {}
for genre in genre_seeds:
    recommendations = sp.recommendations(seed_genres=[genre], limit=1)
    genre_popularity[genre] = recommendations['tracks'][0]['popularity']

# Sort genres by popularity in descending order
sorted_genres = sorted(genre_popularity, key=genre_popularity.get, reverse=True)

# Retrieve the top three genres
top_genres = sorted_genres[:3]

# Print the top genres
print("Top Genres:")
for genre in top_genres:
    print(genre) 