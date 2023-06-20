import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
#PREMISE OF CODE: input artists name, and it will produce all music genres they are associated with
# Spotify API credentials
from api_keys import client_id
from api_keys import client_secret
client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# ENTER <artist's name>
artist_name = input("Enter the artist's name: ")

# Search for the artist on Spotify
results = sp.search(q='artist:' + artist_name, type='artist', limit=1)

# Retrieve the genre information for the artist in the search results and print
if results['artists']['items']:
    artist = results['artists']['items'][0]
    genres = artist['genres']
    if genres:
        print(f"The genre(s) of {artist_name} is/are: {', '.join(genres)}")
    else:
        print(f"No genre information found for {artist_name}.")
else:
    print(f"No artist found with the name {artist_name}.")