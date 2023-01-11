import requests
import vlc
import random

# Spotify Web API endpoint
endpoint = "https://api.spotify.com/v1/browse/new-releases"

# Headers for the API request
headers = {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
    'Authorization': 'Bearer YOUR_ACCESS_TOKEN'
}

# List of countries to select from
countries = ["US","BR","IT","CH","CN","AR"]

# Function to get a random song from a random country
def get_song():
    # Randomly select a country
    country = random.choice(countries)

    # Make a request to the Spotify Web API to get new releases
    params = {
        "country": country,
    }
    response = requests.get(endpoint, headers=headers, params=params)
    data = response.json()

    # Get a random album from the list of new releases
    album = random.choice(data["albums"]["items"])

    # Get a random track from the album
    track = random.choice(album["tracks"]["items"])
    song_name = track["name"]
    artist_name = track["artists"][0]["name"]
    album_name = album["name"]

    # Print the song and artist name
    print("Song:", song_name)
    print("Artist:",artist_name)
    print("Album:",album_name)

    return track["preview_url"]

# Get random song from a random country
song_url = get_song()

# Play the song using vlc
Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(song_url)
Media.get_mrl()
player.set_media(Media)
player.play()
