import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()
url = "https://spotify23.p.rapidapi.com/playlist_tracks/"

querystring = {"id": "37i9dQZF1DX4Wsb4d7NKfP", "offset": "0", "limit": "100"}

headers = {
    "x-rapidapi-key": os.getenv("RAPIDAPI_KEY"),
    "x-rapidapi-host": os.getenv("RAPIDAPI_HOST")
}

def extract_transform():
	response = requests.get(url, headers=headers, params=querystring)
	results = response.json()
	data = []
	artists = []
	songs = []
	for item in range(len(results['items'])):
		album_data = results['items'][item]['track']['album']
		artists_data = results['items'][item]['track']['artists']
		songs_data = results['items'][item]['track']
		songs_date = results['items'][item]
		for artist in range(len(artists_data)):
			artists.append({'artist_id': artists_data[artist]['id'], 'artist_external_url': artists_data[artist]['external_urls']['spotify'], 'artist_name': artists_data[artist]['name']})
		data.append({'album_id': album_data['id'], 'album_name': album_data['name'], 'release_date': album_data['release_date'], 'total_tracks': album_data['total_tracks'], 'external_urls': album_data['external_urls']['spotify']})
		songs.append({'song_id': songs_data['id'], 'song_name': songs_data['name'], 'song_duration': songs_data['duration_ms'], 'song_url': songs_data['external_urls']['spotify'], 'added_at': songs_date['added_at'],
					  'song_popularity': songs_data['popularity'], 'album_id': album_data['id']})
	extracted_data_albums = pd.DataFrame(data)
	extracted_data_artists = pd.DataFrame(artists)
	extracted_songs = pd.DataFrame(songs)

	# Transformation
	extracted_data_albums['release_date'] = pd.to_datetime(extracted_data_albums['release_date'])
	extracted_songs['added_at'] = pd.to_datetime(extracted_songs['added_at'])
	return extracted_data_albums, extracted_data_artists, extracted_songs

# Calling the function
albums, artists, songs = extract_transform()