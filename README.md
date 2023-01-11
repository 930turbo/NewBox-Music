# NewBox

This program starts by importing the necessary libraries: requests, vlc and random, and set up the Spotify Web API endpoint, headers and a list of countries.
Then, it defines a function called get_song() that randomly selects a country from the list and use it to make a request to the Spotify Web API to get new releases. Using the json data, it randomly select an album and a song, prints the song name, artist name and album name and returns the song preview url.

Finally, it calls the get_song function and assigns the return to the variable song_url, after that it uses the vlc library to play the song, by instantiating a vlc player, setting it's media and then playing it.

It's important to notice that, this program needs a Spotify API token, which is a way for the API to identify the developer making the requests and control the rate limit and the access. Also, in order to play the song using vlc, you need to have the vlc media player installed in your machine.
