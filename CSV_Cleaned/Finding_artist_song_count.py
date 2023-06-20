import os
import csv
spotify_csv = os.path.join(".","CSV_Cleaned","Spotify_final_dataset.csv")

def find_artist(artist_name):
    with open(spotify_csv) as csvfile:
        csvreader=csv.reader(csvfile, delimiter=",")
        for line in csvreader:
            if artist_name.lower() in line[1].lower():
                return line
        return "Artist not found"

# Prompt for artist name
artist_name = input("Enter artist name: ")

# Find and print the line containing the artist's first appearance
result = find_artist(artist_name)
print(result)