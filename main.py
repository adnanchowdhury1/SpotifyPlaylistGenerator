from json import JSONDecodeError

import requests
import json


endpoint_url = "https://api.spotify.com/v1/recommendations?"
token = "<<Replace with a Spotify API OAuth token>>"
user_id = "<<Replace with your Spotify username>>"
playlist_name = input("Enter a name for the playlist: ")
playlist_description = input("Enter a description for the playlist: ")
limit = input("Enter the number of songs to be added to the playlist: ")
market = "US"
seed_genres = input("Enter the genres of music to be added to the playlist (if multiple genres, seperate by commas): ")
arr = []

query = f'{endpoint_url}limit={limit}&market={market}&seed_genres={seed_genres}'

response = requests.get(query,
                        headers={"Content-Type": "application/json",
                                 "Authorization": f"Bearer {token}"})
json_response = response.json()

print('Recommended Songs:')
for i, j in enumerate(json_response['tracks']):
    arr.append(j['uri'])
    print(f"{i + 1}) \"{j['name']}\" by {j['artists'][0]['name']}")





endpoint_url = f"https://api.spotify.com/v1/users/{user_id}/playlists"

request_body = json.dumps({
    "name": f"{playlist_name}",
    "description": f"{playlist_description}",
    "public": False
})

response = requests.post(url = endpoint_url, data = request_body, headers={"Content-Type":"application/json",
                        "Authorization":f"Bearer {token}"})


url = response.json()['external_urls']['spotify']

if (response.status_code == 201):
    print("Successfully Created Playlist")
else:
    print("Failed to Create Playlist")




playlist_id = response.json()['id']

endpoint_url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"

request_body = json.dumps({
    "uris": arr
})
response = requests.post(url=endpoint_url, data=request_body, headers={"Content-Type": "application/json",
                                                                       "Authorization": f"Bearer {token}"})


if (response.status_code == 201):
    print("Successfully Added Songs to Playlist")
else:
    print("Failed to Add Songs to Playlist")
