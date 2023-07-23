import spotipy
import requests

spotify_client = spotify_client
spotify_secret = spotify_secret
spotify = spotipy.oauth2.SpotifyOAuth(scope="playlist-modify-private", client_id=spotify_client, client_secret=spotify_secret, redirect_uri="https://example.com", cache_path="token.txt")

sp = spotipy.client.Spotify(auth_manager=spotify)
track = sp.search("track:Sanctuary artist:Joji", limit=1, type="track")
print(track["tracks"]["items"][0]["external_urls"]["spotify"])

# requests.post("https://api.spotify.com/v1/users/989ucp29eddsikxpnaxflcxhr/playlists")