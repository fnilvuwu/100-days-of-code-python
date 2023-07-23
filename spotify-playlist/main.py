from bs4 import BeautifulSoup 
import requests
import spotipy
import requests

spotify_client = spotify_client
spotify_secret = spotify_secret
spotify = spotipy.oauth2.SpotifyOAuth(scope="playlist-modify-private", client_id=spotify_client, client_secret=spotify_secret, redirect_uri="https://example.com", cache_path="token.txt")
# input("Which year do you want to travel to? Type the data in this format YYYY-MM-DD")
URL = "https://www.billboard.com/charts/hot-100/2000-08-12/"

response = requests.get(URL)
song_billboard_web = response.text

song_title_list = []
soup = BeautifulSoup(song_billboard_web, "html.parser")
song_title_list = soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet", id="title-of-a-story") + soup.find_all(name="h3", class_="c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only", id="title-of-a-story")
song_singer_list = soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only u-font-size-20@tablet") + soup.find_all(name="span", class_="c-label a-no-trucate a-font-primary-s lrv-u-font-size-14@mobile-max u-line-height-normal@mobile-max u-letter-spacing-0021 lrv-u-display-block a-truncate-ellipsis-2line u-max-width-330 u-max-width-230@tablet-only")

song_title_list = [song.getText().replace("\n", "").strip() for song in song_title_list]
song_singer_list = [singer.getText().replace("\n", "").strip() for singer in song_singer_list]

sp = spotipy.client.Spotify(auth_manager=spotify)
# sp.user_playlist_create(user="989ucp29eddsikxpnaxflcxhr", name="Top 100 Billboard 2000", public=False)
# print(sp.user_playlist_create(user="989ucp29eddsikxpnaxflcxhr", name="Top 100 Billboard 2000", public=False))
# 7kEATCmmocXlabDWutFz2Z
with open("song_url.txt", "w") as file:
    playlist_id = sp.user_playlist_create(user=user_id, name="Top 100 Billboard 2000", public=False)["id"]
    track_url_list = []
    for song in song_title_list:
        try:
            artist = song_singer_list[song_title_list.index(song)]
            track = sp.search(f"track:{song} artist:{artist}", limit=1, type="track")
            track_url = track["tracks"]["items"][0]["external_urls"]["spotify"]
            track_url_list.append(track_url)
            # print(track_url)
            # file.write(track["tracks"]["items"][0]["external_urls"]["spotify"] + "\n")
        except:
            continue
    sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist_id, tracks=track_url_list)
    



# print(song_title_list_formatted)